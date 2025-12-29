# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class ListAppGroupsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.ListAppGroupsResponseBodyResult] = None,
        total_count: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the application.
        # 
        # For more information, see [AppGroup](https://help.aliyun.com/document_detail/170000.html).
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
                temp_model = main_models.ListAppGroupsResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListAppGroupsResponseBodyResult(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        charging_way: int = None,
        commodity_code: str = None,
        created: int = None,
        current_version: str = None,
        description: str = None,
        domain: str = None,
        engine_type: str = None,
        expire_on: str = None,
        has_pending_quota_review_task: int = None,
        id: str = None,
        instance_id: str = None,
        lock_mode: str = None,
        locked_by_expiration: int = None,
        name: str = None,
        produced: int = None,
        project_id: str = None,
        quota: main_models.ListAppGroupsResponseBodyResultQuota = None,
        status: str = None,
        switched_time: int = None,
        tags: List[main_models.ListAppGroupsResponseBodyResultTags] = None,
        type: str = None,
        updated: int = None,
    ):
        # The billing method. Valid values:
        # 
        # *   POSTPAY: pay-as-you-go.
        # *   PREPAY: subscription.
        self.charge_type = charge_type
        # The billable item. Valid values:
        # 
        # *   1: computing resources.
        # *   2: queries per second (QPS).
        self.charging_way = charging_way
        # The commodity code.
        self.commodity_code = commodity_code
        # The timestamp when the application was created.
        self.created = created
        # The ID of the current online version.
        self.current_version = current_version
        # The description of the application.
        self.description = description
        # The industry of the application.
        self.domain = domain
        # The engine type.
        self.engine_type = engine_type
        # The time when the application expired.
        self.expire_on = expire_on
        # The approval state of the quotas. Valid values:
        # 
        # *   0: The application is in service.
        # *   1: The quotas are being reviewed.
        self.has_pending_quota_review_task = has_pending_quota_review_task
        # The application ID.
        self.id = id
        # The instance ID.
        self.instance_id = instance_id
        # The lock state. Valid values:
        # 
        # *   Unlock: The instance is unlocked.
        # *   LockByExpiration: The instance is automatically locked after it expires.
        # *   ManualLock: The instance is manually locked.
        self.lock_mode = lock_mode
        # Indicates whether the instance is automatically locked after it expires.
        self.locked_by_expiration = locked_by_expiration
        # The application name.
        self.name = name
        # Indicates whether the application is created. Valid values:
        # 
        # *   0: The application is being created.
        # *   1: The application is created.
        self.produced = produced
        # The name of the A/B test group.
        self.project_id = project_id
        # The information about the quotas of the application. For more information, see [Quota](https://help.aliyun.com/document_detail/170001.html).
        self.quota = quota
        # The state of the application. Valid values:
        # 
        # *   producing: The application is being created.
        # *   review_pending: The application is being reviewed.
        # *   config_pending: The application is to be configured.
        # *   normal: The application is in service.
        # *   frozen: The application is frozen.
        self.status = status
        # The timestamp when the current online version was published.
        self.switched_time = switched_time
        # The application tags.
        self.tags = tags
        # The type of the application. Valid values:
        # 
        # *   standard: a High-performance Search Edition application.
        # *   enhanced: an Industry Algorithm Edition application.
        self.type = type
        # The timestamp when the application was last updated.
        self.updated = updated

    def validate(self):
        if self.quota:
            self.quota.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type

        if self.charging_way is not None:
            result['chargingWay'] = self.charging_way

        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code

        if self.created is not None:
            result['created'] = self.created

        if self.current_version is not None:
            result['currentVersion'] = self.current_version

        if self.description is not None:
            result['description'] = self.description

        if self.domain is not None:
            result['domain'] = self.domain

        if self.engine_type is not None:
            result['engineType'] = self.engine_type

        if self.expire_on is not None:
            result['expireOn'] = self.expire_on

        if self.has_pending_quota_review_task is not None:
            result['hasPendingQuotaReviewTask'] = self.has_pending_quota_review_task

        if self.id is not None:
            result['id'] = self.id

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.lock_mode is not None:
            result['lockMode'] = self.lock_mode

        if self.locked_by_expiration is not None:
            result['lockedByExpiration'] = self.locked_by_expiration

        if self.name is not None:
            result['name'] = self.name

        if self.produced is not None:
            result['produced'] = self.produced

        if self.project_id is not None:
            result['projectId'] = self.project_id

        if self.quota is not None:
            result['quota'] = self.quota.to_map()

        if self.status is not None:
            result['status'] = self.status

        if self.switched_time is not None:
            result['switchedTime'] = self.switched_time

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['type'] = self.type

        if self.updated is not None:
            result['updated'] = self.updated

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')

        if m.get('chargingWay') is not None:
            self.charging_way = m.get('chargingWay')

        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')

        if m.get('created') is not None:
            self.created = m.get('created')

        if m.get('currentVersion') is not None:
            self.current_version = m.get('currentVersion')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('domain') is not None:
            self.domain = m.get('domain')

        if m.get('engineType') is not None:
            self.engine_type = m.get('engineType')

        if m.get('expireOn') is not None:
            self.expire_on = m.get('expireOn')

        if m.get('hasPendingQuotaReviewTask') is not None:
            self.has_pending_quota_review_task = m.get('hasPendingQuotaReviewTask')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('lockMode') is not None:
            self.lock_mode = m.get('lockMode')

        if m.get('lockedByExpiration') is not None:
            self.locked_by_expiration = m.get('lockedByExpiration')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('produced') is not None:
            self.produced = m.get('produced')

        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')

        if m.get('quota') is not None:
            temp_model = main_models.ListAppGroupsResponseBodyResultQuota()
            self.quota = temp_model.from_map(m.get('quota'))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('switchedTime') is not None:
            self.switched_time = m.get('switchedTime')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.ListAppGroupsResponseBodyResultTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('updated') is not None:
            self.updated = m.get('updated')

        return self

class ListAppGroupsResponseBodyResultTags(DaraModel):
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
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class ListAppGroupsResponseBodyResultQuota(DaraModel):
    def __init__(
        self,
        compute_resource: int = None,
        doc_size: int = None,
        spec: str = None,
    ):
        # The computing resources. Unit: logical computing unit (LCU).
        self.compute_resource = compute_resource
        # The storage capacity. Unit: GB.
        self.doc_size = doc_size
        # The specifications. Valid values:
        # 
        # *   opensearch.share.junior: basic.
        # *   opensearch.share.common: shared general-purpose.
        # *   opensearch.share.compute: shared computing.
        # *   opensearch.share.storage: shared storage.
        # *   opensearch.private.common: exclusive general-purpose.
        # *   opensearch.private.compute: exclusive computing.
        # *   opensearch.private.storage: exclusive storage.
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compute_resource is not None:
            result['computeResource'] = self.compute_resource

        if self.doc_size is not None:
            result['docSize'] = self.doc_size

        if self.spec is not None:
            result['spec'] = self.spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('computeResource') is not None:
            self.compute_resource = m.get('computeResource')

        if m.get('docSize') is not None:
            self.doc_size = m.get('docSize')

        if m.get('spec') is not None:
            self.spec = m.get('spec')

        return self

