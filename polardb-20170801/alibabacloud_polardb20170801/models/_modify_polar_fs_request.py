# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyPolarFsRequest(DaraModel):
    def __init__(
        self,
        custom_oss_ak: str = None,
        custom_oss_sk: str = None,
        dbcluster_id: str = None,
        polar_fs_instance_id: str = None,
    ):
        # The custom OSS AccessKey ID. You must specify this parameter together with CustomOssSk when you call the ModifyPolarFs operation. Otherwise, the InvalidCustomIdentityInfo.Malformed (400) error is returned.
        self.custom_oss_ak = custom_oss_ak
        # The custom OSS AccessKey Secret. You must specify this parameter together with CustomOssAk when you call the ModifyPolarFs operation. Otherwise, the InvalidCustomIdentityInfo.Malformed (400) error is returned.
        self.custom_oss_sk = custom_oss_sk
        # The cluster ID.
        # >You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/98094.html) operation to query information about all clusters in the specified region, including cluster IDs.
        self.dbcluster_id = dbcluster_id
        # The PolarFs instance ID.
        self.polar_fs_instance_id = polar_fs_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_oss_ak is not None:
            result['CustomOssAk'] = self.custom_oss_ak

        if self.custom_oss_sk is not None:
            result['CustomOssSk'] = self.custom_oss_sk

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.polar_fs_instance_id is not None:
            result['PolarFsInstanceId'] = self.polar_fs_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomOssAk') is not None:
            self.custom_oss_ak = m.get('CustomOssAk')

        if m.get('CustomOssSk') is not None:
            self.custom_oss_sk = m.get('CustomOssSk')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('PolarFsInstanceId') is not None:
            self.polar_fs_instance_id = m.get('PolarFsInstanceId')

        return self

