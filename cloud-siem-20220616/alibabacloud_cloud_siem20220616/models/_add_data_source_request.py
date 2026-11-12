# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddDataSourceRequest(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        cloud_code: str = None,
        data_source_instance_name: str = None,
        data_source_instance_params: str = None,
        data_source_instance_remark: str = None,
        data_source_type: str = None,
        region_id: str = None,
    ):
        # The ID of the cloud account.
        self.account_id = account_id
        # The code of the multi-cloud provider.
        # 
        # This parameter is required.
        self.cloud_code = cloud_code
        # The name of the data source.
        self.data_source_instance_name = data_source_instance_name
        # The parameters of the data source. The value is a JSON array.
        self.data_source_instance_params = data_source_instance_params
        # The remark of the data source.
        self.data_source_instance_remark = data_source_instance_remark
        # The type of the data source. Valid values:
        # - obs: Huawei Cloud OBS.
        # - wafApi: Tencent Cloud WAF download API. 
        # - ckafka: Tencent Cloud CKafka.
        self.data_source_type = data_source_type
        # The region where the data management center of Threat Analysis is located. You must select the region of the management center based on the region where your assets are located. Valid values:
        # - cn-hangzhou: Assets are located in the Chinese mainland and Hong Kong (China).
        # - ap-southeast-1: Assets are located outside China.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code

        if self.data_source_instance_name is not None:
            result['DataSourceInstanceName'] = self.data_source_instance_name

        if self.data_source_instance_params is not None:
            result['DataSourceInstanceParams'] = self.data_source_instance_params

        if self.data_source_instance_remark is not None:
            result['DataSourceInstanceRemark'] = self.data_source_instance_remark

        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')

        if m.get('DataSourceInstanceName') is not None:
            self.data_source_instance_name = m.get('DataSourceInstanceName')

        if m.get('DataSourceInstanceParams') is not None:
            self.data_source_instance_params = m.get('DataSourceInstanceParams')

        if m.get('DataSourceInstanceRemark') is not None:
            self.data_source_instance_remark = m.get('DataSourceInstanceRemark')

        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

