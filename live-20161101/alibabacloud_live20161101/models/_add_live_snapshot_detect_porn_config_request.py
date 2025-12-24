# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AddLiveSnapshotDetectPornConfigRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        domain_name: str = None,
        interval: int = None,
        oss_bucket: str = None,
        oss_endpoint: str = None,
        oss_object: str = None,
        owner_id: int = None,
        scene: List[str] = None,
        security_token: str = None,
    ):
        # The name of the application to which the live stream belongs.
        # 
        # This parameter is required.
        self.app_name = app_name
        # The main streaming domain.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The interval at which snapshots are captured from the live stream. Valid values: **5 to 3600**. Unit: seconds.
        self.interval = interval
        # The name of the OSS bucket.
        # 
        # After the review is complete, you can search for specific violations in the OSS console based on the callback information. You must create the OSS bucket in advance. For more information, see [Configure content moderation](https://help.aliyun.com/document_detail/199449.html).
        # 
        # This parameter is required.
        self.oss_bucket = oss_bucket
        # The endpoint of the Object Storage Service (OSS) bucket.
        # 
        # After the review is complete, you can search for specific violations in the OSS console based on the callback information. You must configure the OSS endpoint in advance. For more information, see [Configure content moderation](https://help.aliyun.com/document_detail/199449.html).
        # 
        # This parameter is required.
        self.oss_endpoint = oss_endpoint
        # The name of the snapshot that stores violations such as pornographic content and politically sensitive content.
        self.oss_object = oss_object
        self.owner_id = owner_id
        # Scene list detection.
        self.scene = scene
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket

        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint

        if self.oss_object is not None:
            result['OssObject'] = self.oss_object

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.scene is not None:
            result['Scene'] = self.scene

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')

        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')

        if m.get('OssObject') is not None:
            self.oss_object = m.get('OssObject')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

