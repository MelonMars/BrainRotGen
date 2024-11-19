from flask import Flask, request, jsonify, send_file
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import os
import tempfile
from flask_cors import CORS
from moviepy.config import change_settings

change_settings({"IMAGEMAGICK_BINARY": "C:\\Program Files\\ImageMagick-7.1.1-Q16-HDRI\\magick.exe"})

app = Flask(__name__)
CORS(app)

def split_text_into_segments(text, words_per_segment):
    words = text.split()
    return [' '.join(words[i:i + words_per_segment]) for i in range(0, len(words), words_per_segment)]

@app.route('/process-payload', methods=['POST'])
def process_payload():
    try:
        aspect_ratio = request.form.get('aspect_ratio')
        rects = request.form.get('rects')
        text_info = request.form.get('text_info')

        import json
        rects = json.loads(rects) if rects else []
        text_info = json.loads(text_info) if text_info else None

        if aspect_ratio == 'portrait':
            canvas_size = (400, 600)
        else:
            canvas_size = (600, 400)

        videos = []
        for file_key in request.files:
            file = request.files[file_key]
            temp_video_path = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4').name
            file.save(temp_video_path)
            videos.append(VideoFileClip(temp_video_path))

        clips = []

        for i, rect in enumerate(rects):
            if i < len(videos):
                video = videos[i]
                video = video.resize((rect['width'], rect['height']))
                video = video.set_position((rect['x'], rect['y']))
                clips.append(video)

        if text_info:
            text = text_info['text']
            words_per_segment = int(text_info.get('words_per_segment', 1))
            segment_duration = int(text_info.get('segment_duration', 2))

            segments = split_text_into_segments(text, words_per_segment)
            text_clips = []
            for i, segment in enumerate(segments):
                text_clip = TextClip(
                    segment,
                    fontsize=24,
                    color='white',
                    size=(canvas_size[0] - 20, None),
                    method='caption'
                ).set_position((text_info['position']['x'], text_info['position']['y'])).set_duration(segment_duration)
                text_clip = text_clip.set_start(i * segment_duration)
                text_clips.append(text_clip)

            clips.extend(text_clips)

        final_clip = CompositeVideoClip(clips, size=canvas_size)
        output_path = "../composited_video.mp4"
        final_clip.write_videofile(output_path, codec='libx264', fps=24)

        for video in videos:
            os.unlink(video.filename)

        return send_file(output_path, as_attachment=True, download_name='composited_video.mp4')

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=False, port=5000, host='0.0.0.0',)
