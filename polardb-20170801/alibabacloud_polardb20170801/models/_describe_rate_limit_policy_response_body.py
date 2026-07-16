# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeRateLimitPolicyResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeRateLimitPolicyResponseBodyItems] = None,
        page_number: str = None,
        page_record_count: str = None,
        page_size: str = None,
        request_id: str = None,
        total_record_count: str = None,
    ):
        # An array of rate limit policy objects.
        self.items = items
        # The returned page number.
        self.page_number = page_number
        # The number of entries returned on the current page.
        self.page_record_count = page_record_count
        # The number of entries returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of matching entries.
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

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeRateLimitPolicyResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeRateLimitPolicyResponseBodyItems(DaraModel):
    def __init__(
        self,
        gmt_created: str = None,
        gmt_modified: str = None,
        gw_cluster_id: str = None,
        policy_id: str = None,
        policy_type: str = None,
        rate_limit_rpm: str = None,
        rate_limit_tpm: str = None,
        scope_ref_id: str = None,
        scope_type: str = None,
        status: str = None,
    ):
        # The creation time.
        self.gmt_created = gmt_created
        # The modification time.
        self.gmt_modified = gmt_modified
        # The ID of the gateway instance.
        self.gw_cluster_id = gw_cluster_id
        # The ID of the rate limit policy.
        self.policy_id = policy_id
        # The policy type.
        self.policy_type = policy_type
        # The maximum requests per minute (RPM).
        self.rate_limit_rpm = rate_limit_rpm
        # The maximum tokens per minute (TPM).
        self.rate_limit_tpm = rate_limit_tpm
        # The ID of the object within the policy\\"s scope, such as a consumer group or a consumer.
        self.scope_ref_id = scope_ref_id
        # The scope of the policy. Valid values:
        # 
        # - **ConsumerGroup**: The policy applies to a consumer group.
        # 
        # - **Consumer**: The policy applies to a specific consumer.
        self.scope_type = scope_type
        # The status of the policy. Valid values:
        # 
        # - **Enabled**: The policy is enabled.
        # 
        # - **Disabled**: The policy is disabled.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.gw_cluster_id is not None:
            result['GwClusterId'] = self.gw_cluster_id

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        if self.rate_limit_rpm is not None:
            result['RateLimitRpm'] = self.rate_limit_rpm

        if self.rate_limit_tpm is not None:
            result['RateLimitTpm'] = self.rate_limit_tpm

        if self.scope_ref_id is not None:
            result['ScopeRefId'] = self.scope_ref_id

        if self.scope_type is not None:
            result['ScopeType'] = self.scope_type

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('GwClusterId') is not None:
            self.gw_cluster_id = m.get('GwClusterId')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        if m.get('RateLimitRpm') is not None:
            self.rate_limit_rpm = m.get('RateLimitRpm')

        if m.get('RateLimitTpm') is not None:
            self.rate_limit_tpm = m.get('RateLimitTpm')

        if m.get('ScopeRefId') is not None:
            self.scope_ref_id = m.get('ScopeRefId')

        if m.get('ScopeType') is not None:
            self.scope_type = m.get('ScopeType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

