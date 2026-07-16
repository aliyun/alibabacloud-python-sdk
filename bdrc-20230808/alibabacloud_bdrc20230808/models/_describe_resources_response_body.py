# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bdrc20230808 import models as main_models
from darabonba.model import DaraModel

class DescribeResourcesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeResourcesResponseBodyData = None,
        request_id: str = None,
    ):
        # The response data.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeResourcesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeResourcesResponseBodyData(DaraModel):
    def __init__(
        self,
        content: List[main_models.DescribeResourcesResponseBodyDataContent] = None,
        max_results: int = None,
        next_token: str = None,
        total_count: int = None,
    ):
        # The list of returned resources.
        self.content = content
        # The maximum number of resources to return on each page.
        self.max_results = max_results
        # The pagination token to retrieve the next page of results. If this parameter is empty, all results have been returned.
        self.next_token = next_token
        # The total number of resources that match the query criteria. This parameter is optional and is not returned by default.
        self.total_count = total_count

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['Content'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('Content') is not None:
            for k1 in m.get('Content'):
                temp_model = main_models.DescribeResourcesResponseBodyDataContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeResourcesResponseBodyDataContent(DaraModel):
    def __init__(
        self,
        archive_data_size: int = None,
        check_failed_count: int = None,
        cold_archive_data_size: int = None,
        create_time: int = None,
        data_redundancy_type: str = None,
        enable_check: bool = None,
        ia_data_size: int = None,
        product_type: str = None,
        protection_score: int = None,
        protection_score_updated_time: int = None,
        region_id: str = None,
        resource_arn: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        risk_count: int = None,
        standard_data_size: int = None,
        status: str = None,
        storage_class: str = None,
        total_data_size: int = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The amount of data in the Archive storage class.
        self.archive_data_size = archive_data_size
        # The number of failed check items.
        self.check_failed_count = check_failed_count
        # The amount of data in the Cold Archive storage class.
        self.cold_archive_data_size = cold_archive_data_size
        # The UNIX timestamp that indicates when the resource was created.
        self.create_time = create_time
        # The data redundancy type.
        self.data_redundancy_type = data_redundancy_type
        # Indicates whether data protection scoring is enabled for the resource.
        self.enable_check = enable_check
        # The amount of data in the Infrequent Access (IA) storage class.
        self.ia_data_size = ia_data_size
        # The type of the cloud service.
        self.product_type = product_type
        # The data protection score of the resource.
        self.protection_score = protection_score
        # The UNIX timestamp that indicates when the score was last updated.
        self.protection_score_updated_time = protection_score_updated_time
        # The region ID.
        self.region_id = region_id
        # The unique resource ARN.
        self.resource_arn = resource_arn
        # The resource ID.
        self.resource_id = resource_id
        # The name of the resource.
        self.resource_name = resource_name
        # The resource owner ID.
        self.resource_owner_id = resource_owner_id
        # The resource type.
        self.resource_type = resource_type
        # The number of check items with potential risks.
        self.risk_count = risk_count
        # The amount of data in the Standard storage class.
        self.standard_data_size = standard_data_size
        # The resource status.
        self.status = status
        # The storage class of the resource.
        self.storage_class = storage_class
        # The total amount of data.
        self.total_data_size = total_data_size
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The VPC ID.
        self.vpc_id = vpc_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.archive_data_size is not None:
            result['ArchiveDataSize'] = self.archive_data_size

        if self.check_failed_count is not None:
            result['CheckFailedCount'] = self.check_failed_count

        if self.cold_archive_data_size is not None:
            result['ColdArchiveDataSize'] = self.cold_archive_data_size

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.data_redundancy_type is not None:
            result['DataRedundancyType'] = self.data_redundancy_type

        if self.enable_check is not None:
            result['EnableCheck'] = self.enable_check

        if self.ia_data_size is not None:
            result['IaDataSize'] = self.ia_data_size

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.protection_score is not None:
            result['ProtectionScore'] = self.protection_score

        if self.protection_score_updated_time is not None:
            result['ProtectionScoreUpdatedTime'] = self.protection_score_updated_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count

        if self.standard_data_size is not None:
            result['StandardDataSize'] = self.standard_data_size

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class

        if self.total_data_size is not None:
            result['TotalDataSize'] = self.total_data_size

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchiveDataSize') is not None:
            self.archive_data_size = m.get('ArchiveDataSize')

        if m.get('CheckFailedCount') is not None:
            self.check_failed_count = m.get('CheckFailedCount')

        if m.get('ColdArchiveDataSize') is not None:
            self.cold_archive_data_size = m.get('ColdArchiveDataSize')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DataRedundancyType') is not None:
            self.data_redundancy_type = m.get('DataRedundancyType')

        if m.get('EnableCheck') is not None:
            self.enable_check = m.get('EnableCheck')

        if m.get('IaDataSize') is not None:
            self.ia_data_size = m.get('IaDataSize')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('ProtectionScore') is not None:
            self.protection_score = m.get('ProtectionScore')

        if m.get('ProtectionScoreUpdatedTime') is not None:
            self.protection_score_updated_time = m.get('ProtectionScoreUpdatedTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')

        if m.get('StandardDataSize') is not None:
            self.standard_data_size = m.get('StandardDataSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')

        if m.get('TotalDataSize') is not None:
            self.total_data_size = m.get('TotalDataSize')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

