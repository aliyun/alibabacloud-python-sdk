# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitYikeStoryboardJobRequest(DaraModel):
    def __init__(
        self,
        aspect_ratio: str = None,
        exec_mode: str = None,
        file_url: str = None,
        keep_origin_dialogue: bool = None,
        model_params: str = None,
        narration_voice_id: str = None,
        need_caption: bool = None,
        resolution: str = None,
        shot_prompt_lang: str = None,
        shot_prompt_mode: str = None,
        shot_split_mode: str = None,
        skip_failure_shot: bool = None,
        source_type: str = None,
        style_id: str = None,
        title: str = None,
        user_data: str = None,
        video_model: str = None,
    ):
        # The aspect ratio of the output video. Valid values:
        # - 16:9
        # - 9:16
        # - 4:3
        # - 3:4
        self.aspect_ratio = aspect_ratio
        # The execution mode for storyboard generation. Valid values:
        # - FullPipeline: full pipeline generation, which includes storyboard generation and shot video generation.
        # - StoryboardOnly: generates only the storyboard.
        self.exec_mode = exec_mode
        # The OSS URL of the file. The URL must point to a file with a .txt or .doc extension.
        self.file_url = file_url
        # Specifies whether to retain the original dialogue during final video composition. Default value: True.
        self.keep_origin_dialogue = keep_origin_dialogue
        # The model parameters in JSON format.
        # 
        #  "AudioEnable": false disables audio.
        self.model_params = model_params
        # The narration voice ID. Valid values:
        # - sys_GracefulPoisedWoman: mature graceful female
        # - sys_ElderlyWistfulWoman: wistful elderly female
        # - sys_SweetBrightGirl: sweet bright girl
        # - sys_YoungGracefulWoman: gentle graceful female
        # - sys_MaturePoisedWoman: poised mature female
        # - sys_MatureWiseWoman: elegant wise female
        # - sys_CalmDeepMale: calm deep male
        # - sys_SereneIntellect: serene intellectual male
        # - sys_MajesticBaritone: majestic baritone male
        # - sys_GravellySoulful: gravelly soulful male
        # - sys_ClassicYoungMan: classic narration male
        # - sys_WiseYoungMan: wise narration male
        # - sys_ClassicYoungWoman: classic narration female
        # - sys_IntellectualYoungWoman: intellectual narration female
        # - sys_GentleYoungMan: gentle narration male
        # - sys_thoughtfulBoy: thoughtful boy
        # - sys_RichBassMale: rich bass male
        # - sys_ClassicMiddleAgedWoman: classic middle-aged narration female
        self.narration_voice_id = narration_voice_id
        self.need_caption = need_caption
        # The resolution of the output video. Valid values:
        # - 720P
        # - 1080P
        # - 2K
        # - 4K
        self.resolution = resolution
        self.shot_prompt_lang = shot_prompt_lang
        # The storyboard shot generation mode. Valid values:
        # - multi: multi-reference video generation
        # - default: image-to-video generation
        self.shot_prompt_mode = shot_prompt_mode
        # The shot split mode. Valid values:
        # - firstPersonNarration: narration commentary mode
        self.shot_split_mode = shot_split_mode
        # Specifies whether to skip failed shots. Default value: True.
        self.skip_failure_shot = skip_failure_shot
        # The type of the material source. Valid values:
        # - Novel: novel
        self.source_type = source_type
        # The storyboard style ID. Valid values:
        # - RealisticPhotographyPro: realistic photography Pro
        # - RealisticGuzhuangPro: realistic ancient costume Pro
        # - RealisticXianxiaPro: realistic Xianxia Pro
        # - RealisticWesternPro: Western realistic Pro
        # - RealisticPhotography: realistic photography
        # - RealisticGuzhuang: realistic ancient costume
        # - RealisticXianxia: realistic Xianxia
        # - RealisticWasteland: realistic wasteland
        # - RealisticEra: realistic vintage
        # - GuofengAnime: 2D Chinese-style anime
        # - GuofengAnime3D: 3D Chinese-style anime
        # - AncientRomanceAnime: anime ancient romance
        # - PostApocalypticAnime: anime post-apocalyptic
        # - Cartoon3D: 3D cartoon
        # - Photorealistic3D: photorealistic 3D rendering
        # - SciFiRealism: sci-fi realism
        # - Chibi3D: 3D chibi
        # - ShojoManga: Japanese manga
        # - NewPeriodAnime: new era Japanese anime
        # - FairyTale2D: 2D fairy tale
        # - Wasteland2D: 2D wasteland
        # - InkWuxia: ink wash Wuxia
        # - ShadiaoMeme: panda head meme style
        # - Chibi2D: 2D chibi
        # - Ghibli: Ghibli
        # - SciFiComic: cyberpunk
        # - AmericanSuperhero: American superhero
        self.style_id = style_id
        # The task title. If not specified, a default title is automatically generated based on the date. The title cannot exceed 128 bytes in length and must be UTF-8 encoded.
        self.title = title
        # The custom settings in JSON format. Fields include:
        # - NotifyAddress: the callback URL for task completion. MNS callbacks and HTTP callbacks are supported.
        self.user_data = user_data
        # The video model. Valid values:
        # - wan2.6-r2v-flash
        self.video_model = video_model

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aspect_ratio is not None:
            result['AspectRatio'] = self.aspect_ratio

        if self.exec_mode is not None:
            result['ExecMode'] = self.exec_mode

        if self.file_url is not None:
            result['FileURL'] = self.file_url

        if self.keep_origin_dialogue is not None:
            result['KeepOriginDialogue'] = self.keep_origin_dialogue

        if self.model_params is not None:
            result['ModelParams'] = self.model_params

        if self.narration_voice_id is not None:
            result['NarrationVoiceId'] = self.narration_voice_id

        if self.need_caption is not None:
            result['NeedCaption'] = self.need_caption

        if self.resolution is not None:
            result['Resolution'] = self.resolution

        if self.shot_prompt_lang is not None:
            result['ShotPromptLang'] = self.shot_prompt_lang

        if self.shot_prompt_mode is not None:
            result['ShotPromptMode'] = self.shot_prompt_mode

        if self.shot_split_mode is not None:
            result['ShotSplitMode'] = self.shot_split_mode

        if self.skip_failure_shot is not None:
            result['SkipFailureShot'] = self.skip_failure_shot

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.style_id is not None:
            result['StyleId'] = self.style_id

        if self.title is not None:
            result['Title'] = self.title

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.video_model is not None:
            result['VideoModel'] = self.video_model

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AspectRatio') is not None:
            self.aspect_ratio = m.get('AspectRatio')

        if m.get('ExecMode') is not None:
            self.exec_mode = m.get('ExecMode')

        if m.get('FileURL') is not None:
            self.file_url = m.get('FileURL')

        if m.get('KeepOriginDialogue') is not None:
            self.keep_origin_dialogue = m.get('KeepOriginDialogue')

        if m.get('ModelParams') is not None:
            self.model_params = m.get('ModelParams')

        if m.get('NarrationVoiceId') is not None:
            self.narration_voice_id = m.get('NarrationVoiceId')

        if m.get('NeedCaption') is not None:
            self.need_caption = m.get('NeedCaption')

        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')

        if m.get('ShotPromptLang') is not None:
            self.shot_prompt_lang = m.get('ShotPromptLang')

        if m.get('ShotPromptMode') is not None:
            self.shot_prompt_mode = m.get('ShotPromptMode')

        if m.get('ShotSplitMode') is not None:
            self.shot_split_mode = m.get('ShotSplitMode')

        if m.get('SkipFailureShot') is not None:
            self.skip_failure_shot = m.get('SkipFailureShot')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('StyleId') is not None:
            self.style_id = m.get('StyleId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('VideoModel') is not None:
            self.video_model = m.get('VideoModel')

        return self

