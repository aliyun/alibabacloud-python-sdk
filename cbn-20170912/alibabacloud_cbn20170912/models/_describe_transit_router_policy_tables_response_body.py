# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class DescribeTransitRouterPolicyTablesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        policy_tables: List[main_models.DescribeTransitRouterPolicyTablesResponseBodyPolicyTables] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The number of entries returned on each page.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results. Valid values:
        # 
        # If NextToken is empty, no next query is to be sent.
        # If NextToken is returned, the value indicates the token that is used to start the next query.
        self.next_token = next_token
        # The policy route tables.
        self.policy_tables = policy_tables
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.policy_tables:
            for v1 in self.policy_tables:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['PolicyTables'] = []
        if self.policy_tables is not None:
            for k1 in self.policy_tables:
                result['PolicyTables'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.policy_tables = []
        if m.get('PolicyTables') is not None:
            for k1 in m.get('PolicyTables'):
                temp_model = main_models.DescribeTransitRouterPolicyTablesResponseBodyPolicyTables()
                self.policy_tables.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeTransitRouterPolicyTablesResponseBodyPolicyTables(DaraModel):
    def __init__(
        self,
        attachments: List[str] = None,
        creation_time: str = None,
        description: str = None,
        name: str = None,
        policy_table_id: str = None,
        region_id: str = None,
        status: str = None,
        tags: List[main_models.DescribeTransitRouterPolicyTablesResponseBodyPolicyTablesTags] = None,
        transit_router_id: str = None,
    ):
        # The attachments associated with the policy route table.
        self.attachments = attachments
        # The time when the policy route table was created. The time is displayed in UTC and follows the ISO 8601 standard in the YYYY-MM-DDThh:mmZ format.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.creation_time = creation_time
        # The description of the policy route table.
        self.description = description
        # The name of the policy route table.
        self.name = name
        # The ID of the policy route table instance.
        self.policy_table_id = policy_table_id
        # The region ID.
        self.region_id = region_id
        # The status of the policy route table. Valid values:
        # 
        # - Creating: The policy route table is being created.
        # 
        # - Active: The policy route table is running.
        # 
        # - Deleting: The policy route table is being deleted.
        self.status = status
        # The tags that are added to the policy route table.
        self.tags = tags
        # The ID of the Enterprise Edition transit router.
        self.transit_router_id = transit_router_id

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
        if self.attachments is not None:
            result['Attachments'] = self.attachments

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.policy_table_id is not None:
            result['PolicyTableId'] = self.policy_table_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attachments') is not None:
            self.attachments = m.get('Attachments')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PolicyTableId') is not None:
            self.policy_table_id = m.get('PolicyTableId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeTransitRouterPolicyTablesResponseBodyPolicyTablesTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        return self

class DescribeTransitRouterPolicyTablesResponseBodyPolicyTablesTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

