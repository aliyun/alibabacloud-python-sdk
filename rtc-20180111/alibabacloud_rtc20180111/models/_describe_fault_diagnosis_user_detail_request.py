# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeFaultDiagnosisUserDetailRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        created_ts: int = None,
        fault_type: str = None,
        query_call_user_info: bool = None,
        user_id: str = None,
    ):
        # APP ID。
        # 
        # This parameter is required.
        self.app_id = app_id
        # 频道ID
        # 
        # This parameter is required.
        self.channel_id = channel_id
        # 频道创建时间，使用UNIX时间戳表示，单位：秒。
        # 
        # This parameter is required.
        self.created_ts = created_ts
        # 异常类型。取值：
        # - **JOIN_SLOW**：进频道慢 。
        # - **AUDIO_STUCK**：音频卡顿。
        # - **VIDEO_STUCK**：视频卡顿。
        # - **VIDEO_VAGUE**：视频模糊。
        # - **HIGH_DELAY**：通话延迟高 。
        # - **FIRST_FRAME_SLOW**：接收首屏慢。
        # 
        # This parameter is required.
        self.fault_type = fault_type
        # 是否查询通话用户信息，为空默认是false。
        self.query_call_user_info = query_call_user_info
        # 用户ID
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts

        if self.fault_type is not None:
            result['FaultType'] = self.fault_type

        if self.query_call_user_info is not None:
            result['QueryCallUserInfo'] = self.query_call_user_info

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')

        if m.get('FaultType') is not None:
            self.fault_type = m.get('FaultType')

        if m.get('QueryCallUserInfo') is not None:
            self.query_call_user_info = m.get('QueryCallUserInfo')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

