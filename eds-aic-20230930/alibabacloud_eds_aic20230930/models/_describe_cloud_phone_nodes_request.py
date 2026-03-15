# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class DescribeCloudPhoneNodesRequest(DaraModel):
    def __init__(
        self,
        bandwidth_package_id: str = None,
        biz_region_id: str = None,
        charge_type: str = None,
        max_results: str = None,
        next_token: str = None,
        node_ids: List[str] = None,
        node_name: str = None,
        node_name_list: List[str] = None,
        server_type: str = None,
        status: str = None,
        tags: List[main_models.DescribeCloudPhoneNodesRequestTags] = None,
    ):
        self.bandwidth_package_id = bandwidth_package_id
        # The region ID.
        self.biz_region_id = biz_region_id
        # The billing method. Only the subscription billing method is supported.
        self.charge_type = charge_type
        # The maximum number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. If a query doesn\\"t return all results, the response includes a NextToken value for pagination. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The matrix IDs.
        self.node_ids = node_ids
        # The matrix name.
        self.node_name = node_name
        self.node_name_list = node_name_list
        # The matrix specification.
        # 
        # Valid values:
        # 
        # *   cpm.gn6.gx1
        self.server_type = server_type
        # The matrix status.
        # 
        # Valid values:
        # 
        # *   FAILED: The matrix failed to be created.
        # *   RUNNING: The matrix is available.
        # *   DELETING: The matrix is being deleted.
        # *   NODE_READY: The matrix is ready, and cloud phone instances are being created.
        # *   DELETED: The matrix is deleted.
        # *   CREATING: The matrix is being created.
        self.status = status
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id

        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.node_name_list is not None:
            result['NodeNameList'] = self.node_name_list

        if self.server_type is not None:
            result['ServerType'] = self.server_type

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('NodeNameList') is not None:
            self.node_name_list = m.get('NodeNameList')

        if m.get('ServerType') is not None:
            self.server_type = m.get('ServerType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeCloudPhoneNodesRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class DescribeCloudPhoneNodesRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

