# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class ListWorkspacesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        workspaces: List[main_models.ListWorkspacesResponseBodyWorkspaces] = None,
    ):
        # The maximum number of entries returned.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The queried workspaces.
        self.workspaces = workspaces

    def validate(self):
        if self.workspaces:
            for v1 in self.workspaces:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        result['workspaces'] = []
        if self.workspaces is not None:
            for k1 in self.workspaces:
                result['workspaces'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        self.workspaces = []
        if m.get('workspaces') is not None:
            for k1 in m.get('workspaces'):
                temp_model = main_models.ListWorkspacesResponseBodyWorkspaces()
                self.workspaces.append(temp_model.from_map(k1))

        return self

class ListWorkspacesResponseBodyWorkspaces(DaraModel):
    def __init__(
        self,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        auto_renew_period_unit: str = None,
        create_time: int = None,
        dlf_catalog_id: str = None,
        dlf_type: str = None,
        duration: int = None,
        end_time: int = None,
        fail_reason: str = None,
        payment_duration_unit: str = None,
        payment_status: str = None,
        payment_type: str = None,
        pre_paid_quota: main_models.ListWorkspacesResponseBodyWorkspacesPrePaidQuota = None,
        region_id: str = None,
        release_type: str = None,
        resource_spec: str = None,
        state_change_reason: main_models.ListWorkspacesResponseBodyWorkspacesStateChangeReason = None,
        storage: str = None,
        tags: List[main_models.ListWorkspacesResponseBodyWorkspacesTags] = None,
        workspace_id: str = None,
        workspace_name: str = None,
        workspace_status: str = None,
    ):
        # Specifies whether to enable auto-renewal. This parameter is required only if the paymentType parameter is set to Pre.
        self.auto_renew = auto_renew
        # The auto-renewal duration. This parameter is required only if the paymentType parameter is set to Pre.
        self.auto_renew_period = auto_renew_period
        # The unit of the auto-renewal duration. This parameter is required only if the paymentType parameter is set to Pre.
        self.auto_renew_period_unit = auto_renew_period_unit
        # The time when the workflow was created.
        self.create_time = create_time
        # The information of the Data Lake Formation (DLF) catalog.
        self.dlf_catalog_id = dlf_catalog_id
        # The version of DLF.
        self.dlf_type = dlf_type
        # The subscription period. This parameter is required only if the paymentType parameter is set to Pre.
        self.duration = duration
        # The end of the end time range.
        self.end_time = end_time
        # The failure reason.
        self.fail_reason = fail_reason
        # The unit of the subscription duration.
        self.payment_duration_unit = payment_duration_unit
        # The status of the payment.
        self.payment_status = payment_status
        # The billing method. Valid values:
        # 
        # - PayAsYouGo
        # - Pre
        self.payment_type = payment_type
        # The information about the subscription quota.
        self.pre_paid_quota = pre_paid_quota
        # The region ID.
        self.region_id = region_id
        # The reason why the workspace is released.
        self.release_type = release_type
        # The resource specifications.
        self.resource_spec = resource_spec
        # The reason of the job status change.
        self.state_change_reason = state_change_reason
        # The OSS path.
        self.storage = storage
        self.tags = tags
        # The workspace ID.
        self.workspace_id = workspace_id
        # The name of the workspace.
        self.workspace_name = workspace_name
        # The workspace status.
        self.workspace_status = workspace_status

    def validate(self):
        if self.pre_paid_quota:
            self.pre_paid_quota.validate()
        if self.state_change_reason:
            self.state_change_reason.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew

        if self.auto_renew_period is not None:
            result['autoRenewPeriod'] = self.auto_renew_period

        if self.auto_renew_period_unit is not None:
            result['autoRenewPeriodUnit'] = self.auto_renew_period_unit

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.dlf_catalog_id is not None:
            result['dlfCatalogId'] = self.dlf_catalog_id

        if self.dlf_type is not None:
            result['dlfType'] = self.dlf_type

        if self.duration is not None:
            result['duration'] = self.duration

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.fail_reason is not None:
            result['failReason'] = self.fail_reason

        if self.payment_duration_unit is not None:
            result['paymentDurationUnit'] = self.payment_duration_unit

        if self.payment_status is not None:
            result['paymentStatus'] = self.payment_status

        if self.payment_type is not None:
            result['paymentType'] = self.payment_type

        if self.pre_paid_quota is not None:
            result['prePaidQuota'] = self.pre_paid_quota.to_map()

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.release_type is not None:
            result['releaseType'] = self.release_type

        if self.resource_spec is not None:
            result['resourceSpec'] = self.resource_spec

        if self.state_change_reason is not None:
            result['stateChangeReason'] = self.state_change_reason.to_map()

        if self.storage is not None:
            result['storage'] = self.storage

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        if self.workspace_name is not None:
            result['workspaceName'] = self.workspace_name

        if self.workspace_status is not None:
            result['workspaceStatus'] = self.workspace_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')

        if m.get('autoRenewPeriod') is not None:
            self.auto_renew_period = m.get('autoRenewPeriod')

        if m.get('autoRenewPeriodUnit') is not None:
            self.auto_renew_period_unit = m.get('autoRenewPeriodUnit')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('dlfCatalogId') is not None:
            self.dlf_catalog_id = m.get('dlfCatalogId')

        if m.get('dlfType') is not None:
            self.dlf_type = m.get('dlfType')

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('failReason') is not None:
            self.fail_reason = m.get('failReason')

        if m.get('paymentDurationUnit') is not None:
            self.payment_duration_unit = m.get('paymentDurationUnit')

        if m.get('paymentStatus') is not None:
            self.payment_status = m.get('paymentStatus')

        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')

        if m.get('prePaidQuota') is not None:
            temp_model = main_models.ListWorkspacesResponseBodyWorkspacesPrePaidQuota()
            self.pre_paid_quota = temp_model.from_map(m.get('prePaidQuota'))

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('releaseType') is not None:
            self.release_type = m.get('releaseType')

        if m.get('resourceSpec') is not None:
            self.resource_spec = m.get('resourceSpec')

        if m.get('stateChangeReason') is not None:
            temp_model = main_models.ListWorkspacesResponseBodyWorkspacesStateChangeReason()
            self.state_change_reason = temp_model.from_map(m.get('stateChangeReason'))

        if m.get('storage') is not None:
            self.storage = m.get('storage')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.ListWorkspacesResponseBodyWorkspacesTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        if m.get('workspaceName') is not None:
            self.workspace_name = m.get('workspaceName')

        if m.get('workspaceStatus') is not None:
            self.workspace_status = m.get('workspaceStatus')

        return self

class ListWorkspacesResponseBodyWorkspacesTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['tagKey'] = self.tag_key

        if self.tag_value is not None:
            result['tagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')

        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')

        return self

class ListWorkspacesResponseBodyWorkspacesStateChangeReason(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # The error code.
        self.code = code
        # The error message.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        return self

class ListWorkspacesResponseBodyWorkspacesPrePaidQuota(DaraModel):
    def __init__(
        self,
        allocated_resource: str = None,
        auto_renewal: bool = None,
        create_time: int = None,
        expire_time: int = None,
        instance_id: str = None,
        max_resource: str = None,
        order_id: str = None,
        payment_status: str = None,
        used_resource: str = None,
    ):
        # The amount of resources that are allocated by a subscription quota.
        self.allocated_resource = allocated_resource
        # Indicates whether auto-renewal is enabled for the subscription quota.
        # 
        # *   true
        # *   false
        self.auto_renewal = auto_renewal
        # The creation time of the subscription quota.
        self.create_time = create_time
        # The expiration time of the subscription quota.
        self.expire_time = expire_time
        # The ID of the instance that is generated when you purchase the subscription quota.
        self.instance_id = instance_id
        # The maximum amount of resources that can be used in a subscription quota.
        self.max_resource = max_resource
        self.order_id = order_id
        # The status of the subscription quota. Valid values:
        # 
        # *   NORMAL
        # *   WAIT_FOR_EXPIRE
        # *   EXPIRED
        self.payment_status = payment_status
        # The amount of resources that are used.
        self.used_resource = used_resource

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocated_resource is not None:
            result['allocatedResource'] = self.allocated_resource

        if self.auto_renewal is not None:
            result['autoRenewal'] = self.auto_renewal

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.expire_time is not None:
            result['expireTime'] = self.expire_time

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.max_resource is not None:
            result['maxResource'] = self.max_resource

        if self.order_id is not None:
            result['orderId'] = self.order_id

        if self.payment_status is not None:
            result['paymentStatus'] = self.payment_status

        if self.used_resource is not None:
            result['usedResource'] = self.used_resource

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allocatedResource') is not None:
            self.allocated_resource = m.get('allocatedResource')

        if m.get('autoRenewal') is not None:
            self.auto_renewal = m.get('autoRenewal')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('maxResource') is not None:
            self.max_resource = m.get('maxResource')

        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')

        if m.get('paymentStatus') is not None:
            self.payment_status = m.get('paymentStatus')

        if m.get('usedResource') is not None:
            self.used_resource = m.get('usedResource')

        return self

