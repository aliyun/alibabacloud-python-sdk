# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeKBSyncLinkAttributeResponseBody(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        config: main_models.DescribeKBSyncLinkAttributeResponseBodyConfig = None,
        creation_time: str = None,
        description: str = None,
        im_platform: str = None,
        link_id: str = None,
        link_name: str = None,
        request_id: str = None,
        source_dir: str = None,
        sync_interval_minutes: int = None,
        sync_status: str = None,
    ):
        # The client ID of the source application.
        self.client_id = client_id
        # The synchronization configuration whitelist returned based on the source type. For DINGTALK, UserId can be returned. For FEISHU, FeishuChatMemberStaleTtlSeconds can be returned.
        self.config = config
        # The creation time of the synchronization link.
        self.creation_time = creation_time
        # The description of the synchronization link.
        self.description = description
        # The source channel of the synchronization link. Valid values: OSS, DINGTALK, FEISHU, and SHAREPOINT.
        self.im_platform = im_platform
        # The unique identifier of the synchronization link.
        self.link_id = link_id
        # The name of the synchronization link.
        self.link_name = link_name
        # The request ID.
        self.request_id = request_id
        # The source directory.
        self.source_dir = source_dir
        # The automatic synchronization interval, in minutes.
        self.sync_interval_minutes = sync_interval_minutes
        # The status of the synchronization link.
        self.sync_status = sync_status

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.config is not None:
            result['Config'] = self.config.to_map()

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.im_platform is not None:
            result['ImPlatform'] = self.im_platform

        if self.link_id is not None:
            result['LinkId'] = self.link_id

        if self.link_name is not None:
            result['LinkName'] = self.link_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.source_dir is not None:
            result['SourceDir'] = self.source_dir

        if self.sync_interval_minutes is not None:
            result['SyncIntervalMinutes'] = self.sync_interval_minutes

        if self.sync_status is not None:
            result['SyncStatus'] = self.sync_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('Config') is not None:
            temp_model = main_models.DescribeKBSyncLinkAttributeResponseBodyConfig()
            self.config = temp_model.from_map(m.get('Config'))

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ImPlatform') is not None:
            self.im_platform = m.get('ImPlatform')

        if m.get('LinkId') is not None:
            self.link_id = m.get('LinkId')

        if m.get('LinkName') is not None:
            self.link_name = m.get('LinkName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SourceDir') is not None:
            self.source_dir = m.get('SourceDir')

        if m.get('SyncIntervalMinutes') is not None:
            self.sync_interval_minutes = m.get('SyncIntervalMinutes')

        if m.get('SyncStatus') is not None:
            self.sync_status = m.get('SyncStatus')

        return self

class DescribeKBSyncLinkAttributeResponseBodyConfig(DaraModel):
    def __init__(
        self,
        feishu_chat_member_stale_ttl_seconds: int = None,
        user_id: str = None,
    ):
        # The validity period of the successful snapshot of Lark group members for fallback reuse, in seconds. This parameter is returned only for FEISHU synchronization links. A value of -1 indicates that the snapshot never expires. A value of 0 indicates that snapshot fallback reuse is disabled. A positive integer indicates the maximum age of the snapshot allowed for reuse. The valid value configured for the link is returned. If no value is configured, the default value -1 is returned.
        self.feishu_chat_member_stale_ttl_seconds = feishu_chat_member_stale_ttl_seconds
        # The ID of the DingTalk user who performs the operation. This parameter is returned only for DINGTALK synchronization links.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.feishu_chat_member_stale_ttl_seconds is not None:
            result['FeishuChatMemberStaleTtlSeconds'] = self.feishu_chat_member_stale_ttl_seconds

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeishuChatMemberStaleTtlSeconds') is not None:
            self.feishu_chat_member_stale_ttl_seconds = m.get('FeishuChatMemberStaleTtlSeconds')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

