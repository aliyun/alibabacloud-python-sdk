# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class DescribeListAntCloudAuthScenesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        scenes: List[main_models.DescribeListAntCloudAuthScenesResponseBodyScenes] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The list of scenarios.
        self.scenes = scenes

    def validate(self):
        if self.scenes:
            for v1 in self.scenes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Scenes'] = []
        if self.scenes is not None:
            for k1 in self.scenes:
                result['Scenes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.scenes = []
        if m.get('Scenes') is not None:
            for k1 in m.get('Scenes'):
                temp_model = main_models.DescribeListAntCloudAuthScenesResponseBodyScenes()
                self.scenes.append(temp_model.from_map(k1))

        return self

class DescribeListAntCloudAuthScenesResponseBodyScenes(DaraModel):
    def __init__(
        self,
        app_id: int = None,
        bind_mini_program: str = None,
        create_time: str = None,
        creator: str = None,
        degrade_app_scheme: str = None,
        degrade_sub_codes: str = None,
        degrade_type: str = None,
        device_risk_plus: str = None,
        domain: str = None,
        mini_program_name: str = None,
        modifier: str = None,
        platform: str = None,
        return_pic_count: int = None,
        return_video_length: int = None,
        scene_id: int = None,
        scene_name: str = None,
        status: int = None,
        store_image: str = None,
        update_time: str = None,
        use_degrade: str = None,
    ):
        # The application ID.
        self.app_id = app_id
        # Specifies whether to enable mini program binding. Valid values:
        # - **Y**: Enabled.
        # - **N (default)**: Disabled.
        self.bind_mini_program = bind_mini_program
        # The creation time. The value is a UNIX timestamp in milliseconds (ms), such as 1740389697000.
        self.create_time = create_time
        # The creator.
        self.creator = creator
        # The iOS scheme for degradation.
        self.degrade_app_scheme = degrade_app_scheme
        # The list of SubCodes that trigger degradation.
        self.degrade_sub_codes = degrade_sub_codes
        # The degraded authentication type.
        self.degrade_type = degrade_type
        # Specifies whether to enable enhanced device risk detection. Valid values:
        # - **Y**: Enabled.
        # - **N**: Disabled.
        self.device_risk_plus = device_risk_plus
        # The bound domain name.
        self.domain = domain
        # The mini program name.
        self.mini_program_name = mini_program_name
        # The modifier.
        self.modifier = modifier
        # The mini program platform. Valid values:
        # - **WECHAT**: WeChat.
        # - **ALIPAY**: Alipay.
        # - **TIKTOK**: TikTok.
        self.platform = platform
        # The number of evidence face photos (1-5).
        self.return_pic_count = return_pic_count
        # The evidence video duration in seconds.
        self.return_video_length = return_video_length
        # The scenario ID.
        self.scene_id = scene_id
        # The scenario name.
        self.scene_name = scene_name
        # Indicates whether the scenario is enabled. The value is 1.
        self.status = status
        # Specifies whether to deliver files generated during authentication to the customer\\"s OSS. Valid values:
        # - **Y**: Enabled.
        # - **N**: Disabled.
        self.store_image = store_image
        # The last update time of the instance. The value is a UNIX timestamp in milliseconds (ms), such as 1740541510000.
        self.update_time = update_time
        # Specifies whether to enable degraded authentication.
        self.use_degrade = use_degrade

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.bind_mini_program is not None:
            result['BindMiniProgram'] = self.bind_mini_program

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.degrade_app_scheme is not None:
            result['DegradeAppScheme'] = self.degrade_app_scheme

        if self.degrade_sub_codes is not None:
            result['DegradeSubCodes'] = self.degrade_sub_codes

        if self.degrade_type is not None:
            result['DegradeType'] = self.degrade_type

        if self.device_risk_plus is not None:
            result['DeviceRiskPlus'] = self.device_risk_plus

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.mini_program_name is not None:
            result['MiniProgramName'] = self.mini_program_name

        if self.modifier is not None:
            result['Modifier'] = self.modifier

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

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.use_degrade is not None:
            result['UseDegrade'] = self.use_degrade

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('BindMiniProgram') is not None:
            self.bind_mini_program = m.get('BindMiniProgram')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('DegradeAppScheme') is not None:
            self.degrade_app_scheme = m.get('DegradeAppScheme')

        if m.get('DegradeSubCodes') is not None:
            self.degrade_sub_codes = m.get('DegradeSubCodes')

        if m.get('DegradeType') is not None:
            self.degrade_type = m.get('DegradeType')

        if m.get('DeviceRiskPlus') is not None:
            self.device_risk_plus = m.get('DeviceRiskPlus')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('MiniProgramName') is not None:
            self.mini_program_name = m.get('MiniProgramName')

        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')

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

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UseDegrade') is not None:
            self.use_degrade = m.get('UseDegrade')

        return self

