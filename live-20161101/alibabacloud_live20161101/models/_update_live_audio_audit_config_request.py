# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateLiveAudioAuditConfigRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        biz_type: str = None,
        domain_name: str = None,
        oss_bucket: str = None,
        oss_endpoint: str = None,
        oss_object: str = None,
        owner_id: int = None,
        region_id: str = None,
        stream_name: str = None,
    ):
        # The name of the application to which the live stream belongs. The value of this parameter must be the same as the application name in the ingest URL. Otherwise, the configuration does not take effect. The application name is case-sensitive.
        # 
        # This parameter is required.
        self.app_name = app_name
        # The business type. You can specify a model. The default value is the domain name.
        self.biz_type = biz_type
        # The main streaming domain.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The name of the Object Storage Service (OSS) bucket.
        self.oss_bucket = oss_bucket
        # The endpoint of the OSS bucket.
        self.oss_endpoint = oss_endpoint
        # The name of the recording that is stored in OSS.
        self.oss_object = oss_object
        self.owner_id = owner_id
        self.region_id = region_id
        # The name of the live stream. The value of this parameter must be the same as the stream name in the ingest URL. Otherwise, the configuration does not take effect. The stream name is case-sensitive.
        # 
        # This parameter is required.
        self.stream_name = stream_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket

        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint

        if self.oss_object is not None:
            result['OssObject'] = self.oss_object

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')

        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')

        if m.get('OssObject') is not None:
            self.oss_object = m.get('OssObject')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        return self

