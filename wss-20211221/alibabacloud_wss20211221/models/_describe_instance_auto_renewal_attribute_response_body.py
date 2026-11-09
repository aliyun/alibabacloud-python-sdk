# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_wss20211221 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceAutoRenewalAttributeResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        instance_attribute: List[main_models.DescribeInstanceAutoRenewalAttributeResponseBodyInstanceAttribute] = None,
        max_results: int = None,
        next_token: str = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
    ):
        # The total number of entries that meet the query conditions.
        self.count = count
        # The list of instances and their auto-renewal status.
        self.instance_attribute = instance_attribute
        # The maximum number of entries to return per query.
        self.max_results = max_results
        # The mark for paging. Leave this parameter empty for the first query. For subsequent paging, pass the NextToken value returned in the previous response as is. Do not construct or decode the value.
        self.next_token = next_token
        # The page number of the paging query, starting from 1.
        self.page_no = page_no
        # The maximum number of entries returned per page.
        self.page_size = page_size
        # The unique identifier of the request. You can use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.instance_attribute:
            for v1 in self.instance_attribute:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        result['InstanceAttribute'] = []
        if self.instance_attribute is not None:
            for k1 in self.instance_attribute:
                result['InstanceAttribute'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.instance_attribute = []
        if m.get('InstanceAttribute') is not None:
            for k1 in m.get('InstanceAttribute'):
                temp_model = main_models.DescribeInstanceAutoRenewalAttributeResponseBodyInstanceAttribute()
                self.instance_attribute.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeInstanceAutoRenewalAttributeResponseBodyInstanceAttribute(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        auto_renewal: bool = None,
        instance_id: str = None,
    ):
        # The ID of the Alibaba Cloud account to which the resource belongs.
        self.ali_uid = ali_uid
        # The auto-renewal status. Valid values:
        # - true: Auto-renewal is enabled.
        # - false: Auto-renewal is disabled.
        self.auto_renewal = auto_renewal
        # The instance ID, which identifies the purchased instance.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

