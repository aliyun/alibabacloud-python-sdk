# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class ListQuotaReviewTasksResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.ListQuotaReviewTasksResponseBodyResult] = None,
        total_count: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the tickets. For more information, see [QuotaReviewTask](https://help.aliyun.com/document_detail/173609.html).
        self.result = result
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['result'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.result = []
        if m.get('result') is not None:
            for k1 in m.get('result'):
                temp_model = main_models.ListQuotaReviewTasksResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListQuotaReviewTasksResponseBodyResult(DaraModel):
    def __init__(
        self,
        app_group_id: int = None,
        app_group_name: str = None,
        app_group_type: str = None,
        approved: bool = None,
        available: bool = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        memo: str = None,
        new_compute_resource: int = None,
        new_soc_size: int = None,
        new_spec: str = None,
        old_compute_resource: int = None,
        old_doc_size: int = None,
        old_spec: str = None,
        pending: bool = None,
    ):
        # The application ID.
        self.app_group_id = app_group_id
        # The application name.
        self.app_group_name = app_group_name
        # The application type.
        self.app_group_type = app_group_type
        # Indicates whether the ticket is approved.
        self.approved = approved
        # Indicates whether the application is available.
        self.available = available
        # The time when the ticket was created.
        self.gmt_create = gmt_create
        # The time when the ticket was last updated.
        self.gmt_modified = gmt_modified
        # The ticket ID.
        self.id = id
        # The remarks.
        self.memo = memo
        # The computing resource quota that is applied for.
        self.new_compute_resource = new_compute_resource
        # The storage capacity quota that is applied for.
        self.new_soc_size = new_soc_size
        # The application specifications that are applied for.
        self.new_spec = new_spec
        # The original quota of computing resources.
        self.old_compute_resource = old_compute_resource
        # The original quota of storage capacity.
        self.old_doc_size = old_doc_size
        # The original specifications of the application.
        self.old_spec = old_spec
        # Indicates whether the ticket is pending.
        self.pending = pending

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_group_id is not None:
            result['appGroupId'] = self.app_group_id

        if self.app_group_name is not None:
            result['appGroupName'] = self.app_group_name

        if self.app_group_type is not None:
            result['appGroupType'] = self.app_group_type

        if self.approved is not None:
            result['approved'] = self.approved

        if self.available is not None:
            result['available'] = self.available

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.memo is not None:
            result['memo'] = self.memo

        if self.new_compute_resource is not None:
            result['newComputeResource'] = self.new_compute_resource

        if self.new_soc_size is not None:
            result['newSocSize'] = self.new_soc_size

        if self.new_spec is not None:
            result['newSpec'] = self.new_spec

        if self.old_compute_resource is not None:
            result['oldComputeResource'] = self.old_compute_resource

        if self.old_doc_size is not None:
            result['oldDocSize'] = self.old_doc_size

        if self.old_spec is not None:
            result['oldSpec'] = self.old_spec

        if self.pending is not None:
            result['pending'] = self.pending

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appGroupId') is not None:
            self.app_group_id = m.get('appGroupId')

        if m.get('appGroupName') is not None:
            self.app_group_name = m.get('appGroupName')

        if m.get('appGroupType') is not None:
            self.app_group_type = m.get('appGroupType')

        if m.get('approved') is not None:
            self.approved = m.get('approved')

        if m.get('available') is not None:
            self.available = m.get('available')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('memo') is not None:
            self.memo = m.get('memo')

        if m.get('newComputeResource') is not None:
            self.new_compute_resource = m.get('newComputeResource')

        if m.get('newSocSize') is not None:
            self.new_soc_size = m.get('newSocSize')

        if m.get('newSpec') is not None:
            self.new_spec = m.get('newSpec')

        if m.get('oldComputeResource') is not None:
            self.old_compute_resource = m.get('oldComputeResource')

        if m.get('oldDocSize') is not None:
            self.old_doc_size = m.get('oldDocSize')

        if m.get('oldSpec') is not None:
            self.old_spec = m.get('oldSpec')

        if m.get('pending') is not None:
            self.pending = m.get('pending')

        return self

