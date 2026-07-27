# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class CreateBatchConsumerResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.CreateBatchConsumerResponseBodyItems] = None,
        page_number: int = None,
        page_record_count: int = None,
        page_size: int = None,
        request_id: str = None,
        total_pages: int = None,
        total_record_count: int = None,
    ):
        # The list of consumer objects.
        self.items = items
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of records on the current page.
        self.page_record_count = page_record_count
        # The number of records per page. Valid values:
        # * **30**
        # * **50**
        # * **100**
        # 
        # Default value: 30.
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        # The total number of pages.
        self.total_pages = total_pages
        # The total number of records.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.CreateBatchConsumerResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class CreateBatchConsumerResponseBodyItems(DaraModel):
    def __init__(
        self,
        active: bool = None,
        api_key: str = None,
        api_key_md_5: str = None,
        api_key_status: str = None,
        api_status: str = None,
        budget_limit: int = None,
        budget_policy_id: str = None,
        budget_used: int = None,
        consumer_group_id: str = None,
        consumer_id: str = None,
        consumer_tag: str = None,
        description: str = None,
        expire_time: str = None,
        expired: bool = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        gw_cluster_id: str = None,
        name: str = None,
        status: str = None,
    ):
        # Indicates whether the key is active.
        self.active = active
        # The full API key. Returned only in this response.
        self.api_key = api_key
        # The MD5 hash of the API key.
        self.api_key_md_5 = api_key_md_5
        # The status of the API key. Default value: Active.
        self.api_key_status = api_key_status
        # The API key status. Default value: Active.
        self.api_status = api_status
        # The budget limit, which equals the number of credits per package.
        self.budget_limit = budget_limit
        # The budget policy ID. Each key has an independent budget policy.
        self.budget_policy_id = budget_policy_id
        # The used quota.
        self.budget_used = budget_used
        # The user group ID.
        self.consumer_group_id = consumer_group_id
        # The user ID.
        self.consumer_id = consumer_id
        # The consumer tag.
        self.consumer_tag = consumer_tag
        # The application description or remarks.
        self.description = description
        # The expiration time.
        self.expire_time = expire_time
        # Indicates whether the key is expired.
        self.expired = expired
        # The creation time.
        self.gmt_created = gmt_created
        # The last modification time.
        self.gmt_modified = gmt_modified
        # The gateway instance ID.
        self.gw_cluster_id = gw_cluster_id
        # The name.
        self.name = name
        # The consumer status. Default value: Enabled.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active is not None:
            result['Active'] = self.active

        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.api_key_md_5 is not None:
            result['ApiKeyMd5'] = self.api_key_md_5

        if self.api_key_status is not None:
            result['ApiKeyStatus'] = self.api_key_status

        if self.api_status is not None:
            result['ApiStatus'] = self.api_status

        if self.budget_limit is not None:
            result['BudgetLimit'] = self.budget_limit

        if self.budget_policy_id is not None:
            result['BudgetPolicyId'] = self.budget_policy_id

        if self.budget_used is not None:
            result['BudgetUsed'] = self.budget_used

        if self.consumer_group_id is not None:
            result['ConsumerGroupId'] = self.consumer_group_id

        if self.consumer_id is not None:
            result['ConsumerId'] = self.consumer_id

        if self.consumer_tag is not None:
            result['ConsumerTag'] = self.consumer_tag

        if self.description is not None:
            result['Description'] = self.description

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.gw_cluster_id is not None:
            result['GwClusterId'] = self.gw_cluster_id

        if self.name is not None:
            result['Name'] = self.name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')

        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('ApiKeyMd5') is not None:
            self.api_key_md_5 = m.get('ApiKeyMd5')

        if m.get('ApiKeyStatus') is not None:
            self.api_key_status = m.get('ApiKeyStatus')

        if m.get('ApiStatus') is not None:
            self.api_status = m.get('ApiStatus')

        if m.get('BudgetLimit') is not None:
            self.budget_limit = m.get('BudgetLimit')

        if m.get('BudgetPolicyId') is not None:
            self.budget_policy_id = m.get('BudgetPolicyId')

        if m.get('BudgetUsed') is not None:
            self.budget_used = m.get('BudgetUsed')

        if m.get('ConsumerGroupId') is not None:
            self.consumer_group_id = m.get('ConsumerGroupId')

        if m.get('ConsumerId') is not None:
            self.consumer_id = m.get('ConsumerId')

        if m.get('ConsumerTag') is not None:
            self.consumer_tag = m.get('ConsumerTag')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('GwClusterId') is not None:
            self.gw_cluster_id = m.get('GwClusterId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

