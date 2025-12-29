# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAntCloudAuthSceneRequest(DaraModel):
    def __init__(
        self,
        bind_mini_program: str = None,
        check_file_body: str = None,
        check_file_name: str = None,
        mini_program_name: str = None,
        platform: str = None,
        return_pic_count: int = None,
        return_video_length: int = None,
        scene_name: str = None,
        store_image: str = None,
    ):
        # Whether to enable binding of the mini program:
        # - **Y**: Enable
        # - **N (default)**: Not enabled
        self.bind_mini_program = bind_mini_program
        # Content of the uploaded verification file.
        self.check_file_body = check_file_body
        # Name of the uploaded verification file.
        self.check_file_name = check_file_name
        # Mini program name.
        self.mini_program_name = mini_program_name
        # Binding platform for the mini program:
        # - **WECHAT**: WeChat
        # - **ALIPAY**: Alipay
        # - **TIKTOK**: TikTok
        self.platform = platform
        self.return_pic_count = return_pic_count
        self.return_video_length = return_video_length
        # Scene name.
        # 
        # This parameter is required.
        self.scene_name = scene_name
        # Whether to deliver the files generated from the authentication to the customer\\"s OSS:
        # - **Y**: Yes
        # - **N**: No
        self.store_image = store_image

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_mini_program is not None:
            result['BindMiniProgram'] = self.bind_mini_program

        if self.check_file_body is not None:
            result['CheckFileBody'] = self.check_file_body

        if self.check_file_name is not None:
            result['CheckFileName'] = self.check_file_name

        if self.mini_program_name is not None:
            result['MiniProgramName'] = self.mini_program_name

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.return_pic_count is not None:
            result['ReturnPicCount'] = self.return_pic_count

        if self.return_video_length is not None:
            result['ReturnVideoLength'] = self.return_video_length

        if self.scene_name is not None:
            result['SceneName'] = self.scene_name

        if self.store_image is not None:
            result['StoreImage'] = self.store_image

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindMiniProgram') is not None:
            self.bind_mini_program = m.get('BindMiniProgram')

        if m.get('CheckFileBody') is not None:
            self.check_file_body = m.get('CheckFileBody')

        if m.get('CheckFileName') is not None:
            self.check_file_name = m.get('CheckFileName')

        if m.get('MiniProgramName') is not None:
            self.mini_program_name = m.get('MiniProgramName')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('ReturnPicCount') is not None:
            self.return_pic_count = m.get('ReturnPicCount')

        if m.get('ReturnVideoLength') is not None:
            self.return_video_length = m.get('ReturnVideoLength')

        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')

        if m.get('StoreImage') is not None:
            self.store_image = m.get('StoreImage')

        return self

