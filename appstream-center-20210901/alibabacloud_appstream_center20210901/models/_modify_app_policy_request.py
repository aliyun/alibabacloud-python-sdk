# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class ModifyAppPolicyRequest(DaraModel):
    def __init__(
        self,
        app_policy_id: str = None,
        product_type: str = None,
        video_policy: main_models.ModifyAppPolicyRequestVideoPolicy = None,
    ):
        # The policy ID.
        # 
        # This parameter is required.
        self.app_policy_id = app_policy_id
        # The product type.
        # 
        # This parameter is required.
        self.product_type = product_type
        # The display policy.
        self.video_policy = video_policy

    def validate(self):
        if self.video_policy:
            self.video_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_policy_id is not None:
            result['AppPolicyId'] = self.app_policy_id

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.video_policy is not None:
            result['VideoPolicy'] = self.video_policy.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppPolicyId') is not None:
            self.app_policy_id = m.get('AppPolicyId')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('VideoPolicy') is not None:
            temp_model = main_models.ModifyAppPolicyRequestVideoPolicy()
            self.video_policy = temp_model.from_map(m.get('VideoPolicy'))

        return self

class ModifyAppPolicyRequestVideoPolicy(DaraModel):
    def __init__(
        self,
        frame_rate: int = None,
        session_resolution_height: int = None,
        session_resolution_width: int = None,
        streaming_mode: str = None,
        terminal_resolution_adaptive: bool = None,
        visual_quality_strategy: str = None,
        webrtc: bool = None,
    ):
        # The frame rate (FPS).
        self.frame_rate = frame_rate
        # The height of the resolution, in pixels.
        self.session_resolution_height = session_resolution_height
        # The width of the resolution, in pixels.
        self.session_resolution_width = session_resolution_width
        # The streaming mode. This parameter is used together with the Webrtc parameter to specify the protocol type.
        # 
        # - Webrtc=`true` and StreamingMode=`video`: WebRTC stream.
        # - Webrtc=`false` and StreamingMode=`video`: video stream.
        # - Webrtc=`false` and StreamingMode=`mix`: mixed stream.
        self.streaming_mode = streaming_mode
        # Specifies whether to use adaptive resolution.
        # 
        # - `true`: The session resolution follows changes in the terminal display area. In this case, SessionResolutionWidth and SessionResolutionHeight specify the maximum resolution values.
        # 
        # - `false`: The session resolution does not follow changes in the terminal display area. In this case, the resolution is fixed to the values of SessionResolutionWidth and SessionResolutionHeight.
        self.terminal_resolution_adaptive = terminal_resolution_adaptive
        # The visual quality strategy.
        self.visual_quality_strategy = visual_quality_strategy
        # Specifies whether to enable WebRTC. This parameter is used together with the StreamingMode parameter to specify the protocol type.
        # 
        # - Webrtc=`true` and StreamingMode=`video`: WebRTC stream.
        # - Webrtc=`false` and StreamingMode=`video`: video stream.
        # - Webrtc=`false` and StreamingMode=`mix`: mixed stream.
        self.webrtc = webrtc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate

        if self.session_resolution_height is not None:
            result['SessionResolutionHeight'] = self.session_resolution_height

        if self.session_resolution_width is not None:
            result['SessionResolutionWidth'] = self.session_resolution_width

        if self.streaming_mode is not None:
            result['StreamingMode'] = self.streaming_mode

        if self.terminal_resolution_adaptive is not None:
            result['TerminalResolutionAdaptive'] = self.terminal_resolution_adaptive

        if self.visual_quality_strategy is not None:
            result['VisualQualityStrategy'] = self.visual_quality_strategy

        if self.webrtc is not None:
            result['Webrtc'] = self.webrtc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')

        if m.get('SessionResolutionHeight') is not None:
            self.session_resolution_height = m.get('SessionResolutionHeight')

        if m.get('SessionResolutionWidth') is not None:
            self.session_resolution_width = m.get('SessionResolutionWidth')

        if m.get('StreamingMode') is not None:
            self.streaming_mode = m.get('StreamingMode')

        if m.get('TerminalResolutionAdaptive') is not None:
            self.terminal_resolution_adaptive = m.get('TerminalResolutionAdaptive')

        if m.get('VisualQualityStrategy') is not None:
            self.visual_quality_strategy = m.get('VisualQualityStrategy')

        if m.get('Webrtc') is not None:
            self.webrtc = m.get('Webrtc')

        return self

