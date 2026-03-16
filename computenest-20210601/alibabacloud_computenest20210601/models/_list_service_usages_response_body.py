# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_computenest20210601 import models as main_models
from darabonba.model import DaraModel

class ListServiceUsagesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        service_usages: List[main_models.ListServiceUsagesResponseBodyServiceUsages] = None,
        total_count: int = None,
    ):
        # The maximum number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The service applications.
        self.service_usages = service_usages
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.service_usages:
            for v1 in self.service_usages:
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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ServiceUsages'] = []
        if self.service_usages is not None:
            for k1 in self.service_usages:
                result['ServiceUsages'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.service_usages = []
        if m.get('ServiceUsages') is not None:
            for k1 in m.get('ServiceUsages'):
                temp_model = main_models.ListServiceUsagesResponseBodyServiceUsages()
                self.service_usages.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListServiceUsagesResponseBodyServiceUsages(DaraModel):
    def __init__(
        self,
        comments: str = None,
        create_time: str = None,
        service_id: str = None,
        service_name: str = None,
        status: str = None,
        supplier_name: str = None,
        update_time: str = None,
        user_ali_uid: int = None,
        user_information: Dict[str, str] = None,
    ):
        # The review comment.
        self.comments = comments
        # The time when the application was created.
        self.create_time = create_time
        # The service ID.
        self.service_id = service_id
        # The service name.
        self.service_name = service_name
        # The state of the service application. Valid values:
        # 
        # *   Submitted: The application is submitted for review.
        # *   Approved: The application is approved.
        # *   Rejected: The application is rejected.
        # *   Canceled: The application is canceled.
        self.status = status
        # The name of the service provider.
        self.supplier_name = supplier_name
        # The time when the application was updated.
        self.update_time = update_time
        # The ID of the Alibaba Cloud account.
        self.user_ali_uid = user_ali_uid
        # The information about the applicants.
        self.user_information = user_information

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comments is not None:
            result['Comments'] = self.comments

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.status is not None:
            result['Status'] = self.status

        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.user_ali_uid is not None:
            result['UserAliUid'] = self.user_ali_uid

        if self.user_information is not None:
            result['UserInformation'] = self.user_information

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UserAliUid') is not None:
            self.user_ali_uid = m.get('UserAliUid')

        if m.get('UserInformation') is not None:
            self.user_information = m.get('UserInformation')

        return self

