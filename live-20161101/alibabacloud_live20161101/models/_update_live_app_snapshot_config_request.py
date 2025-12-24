# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateLiveAppSnapshotConfigRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        callback: str = None,
        domain_name: str = None,
        oss_bucket: str = None,
        oss_endpoint: str = None,
        overwrite_oss_object: str = None,
        owner_id: int = None,
        security_token: str = None,
        sequence_oss_object: str = None,
        time_interval: int = None,
    ):
        # The name of the application to which the live stream belongs.
        # 
        # This parameter is required.
        self.app_name = app_name
        # The callback URL that is used to receive notifications about snapshot capture.
        self.callback = callback
        # The main streaming domain.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The name of the OSS bucket.
        self.oss_bucket = oss_bucket
        # The endpoint of the OSS bucket.
        self.oss_endpoint = oss_endpoint
        # The naming format of snapshots that are stored in the overwrite mode, which means that a new snapshot overwrites the previous snapshot.
        # 
        # *   The name must be less than 256 bytes in length.
        # *   Only JPG images are supported.
        # *   The name can contain variables such as {AppName} and {StreamName}.
        # *   A value of hyphen (-) indicates that this parameter is deleted.
        self.overwrite_oss_object = overwrite_oss_object
        self.owner_id = owner_id
        self.security_token = security_token
        # The naming format of snapshots that are stored in sequence, which means that a new snapshot does not overwrite the previous snapshot. You can call the [DescribeLiveStreamSnapshotInfo](https://help.aliyun.com/document_detail/2847902.html) operation to query the snapshots that were captured within a specific time period.
        # 
        # *   The name must be less than 256 bytes in length.
        # *   Only JPG images are supported.
        # *   The name can contain variables such as {AppName}, {StreamName}, {UnixTimestamp}, and {Sequence}. The name must contain at least one of the {UnixTimestamp} and {Sequence} variables.
        # *   A value of hyphen (-) indicates that this parameter is deleted.
        self.sequence_oss_object = sequence_oss_object
        # The interval at which snapshots are captured. Valid values: **5 to 3600**. Unit: seconds.
        self.time_interval = time_interval

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.callback is not None:
            result['Callback'] = self.callback

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket

        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint

        if self.overwrite_oss_object is not None:
            result['OverwriteOssObject'] = self.overwrite_oss_object

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.sequence_oss_object is not None:
            result['SequenceOssObject'] = self.sequence_oss_object

        if self.time_interval is not None:
            result['TimeInterval'] = self.time_interval

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Callback') is not None:
            self.callback = m.get('Callback')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')

        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')

        if m.get('OverwriteOssObject') is not None:
            self.overwrite_oss_object = m.get('OverwriteOssObject')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('SequenceOssObject') is not None:
            self.sequence_oss_object = m.get('SequenceOssObject')

        if m.get('TimeInterval') is not None:
            self.time_interval = m.get('TimeInterval')

        return self

