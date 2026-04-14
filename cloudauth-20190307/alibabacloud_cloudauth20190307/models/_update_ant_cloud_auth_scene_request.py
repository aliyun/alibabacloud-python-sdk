# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAntCloudAuthSceneRequest(DaraModel):
    def __init__(
        self,
        bind_mini_program: str = None,
        check_file_body: str = None,
        check_file_name: str = None,
        device_risk_plus: str = None,
        mini_program_name: str = None,
        platform: str = None,
        return_pic_count: int = None,
        return_video_length: int = None,
        scene_id: int = None,
        scene_name: str = None,
        status: int = None,
        store_image: str = None,
    ):
        # Update Ant Blockchain Transaction Scenario
        self.bind_mini_program = bind_mini_program
        # Whether to enable binding with a mini program:
        # - **Y**: Enable
        # - **N (default)**: Disable
        # >Notice: If you enable binding with a mini program, please ensure that all parameters for the mini program are passed.
        self.check_file_body = check_file_body
        # Scenario name.
        self.check_file_name = check_file_name
        # Name of the uploaded verification file.
        self.device_risk_plus = device_risk_plus
        # System-defined parameter. Value: **UpdateAntCloudAuthScene**.
        self.mini_program_name = mini_program_name
        # Currently meaningless, can be omitted.
        self.platform = platform
        # Mini program name.
        self.return_pic_count = return_pic_count
        # Platform for binding the mini program:
        # - **WECHAT**: WeChat
        # - **ALIPAY**: Alipay
        # - **TIKTOK**: TikTok
        self.return_video_length = return_video_length
        # Update Financial-Level Authentication Scenario
        # 
        # This parameter is required.
        self.scene_id = scene_id
        # Update the information of a financial-level authentication scenario based on the scenario ID.
        # - Service address: cloudauth.aliyuncs.com.
        # - Request method: HTTPS POST.
        self.scene_name = scene_name
        # Update Ant Blockchain Transaction Scenario
        self.status = status
        # Update the information of a financial-level authentication scenario based on the scenario ID.
        # - Service address: cloudauth.aliyuncs.com.
        # - Request method: HTTPS POST.
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

        if self.device_risk_plus is not None:
            result['DeviceRiskPlus'] = self.device_risk_plus

        if self.mini_program_name is not None:
            result['MiniProgramName'] = self.mini_program_name

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.return_pic_count is not None:
            result['ReturnPicCount'] = self.return_pic_count

        if self.return_video_length is not None:
            result['ReturnVideoLength'] = self.return_video_length

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.scene_name is not None:
            result['SceneName'] = self.scene_name

        if self.status is not None:
            result['Status'] = self.status

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

        if m.get('DeviceRiskPlus') is not None:
            self.device_risk_plus = m.get('DeviceRiskPlus')

        if m.get('MiniProgramName') is not None:
            self.mini_program_name = m.get('MiniProgramName')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('ReturnPicCount') is not None:
            self.return_pic_count = m.get('ReturnPicCount')

        if m.get('ReturnVideoLength') is not None:
            self.return_video_length = m.get('ReturnVideoLength')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StoreImage') is not None:
            self.store_image = m.get('StoreImage')

        return self

