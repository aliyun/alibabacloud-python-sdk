# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class ListQuotasResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        data: main_models.ListQuotasResponseBodyData = None,
        marker: str = None,
        max_item: int = None,
        quota_info_list: List[main_models.ListQuotasResponseBodyQuotaInfoList] = None,
        request_id: str = None,
    ):
        # The token for the next page of results. This operation supports only consecutive paging. If the returned value is not empty, more data is available. To get the next page, use the returned value in your next request.
        self.next_token = next_token
        # The data returned.
        self.data = data
        # The token that specifies the position from which to start returning results. The results are sorted in alphabetical order.
        self.marker = marker
        # The maximum number of entries returned on each page.
        self.max_item = max_item
        # The list of quotas.
        self.quota_info_list = quota_info_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()
        if self.quota_info_list:
            for v1 in self.quota_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.marker is not None:
            result['marker'] = self.marker

        if self.max_item is not None:
            result['maxItem'] = self.max_item

        result['quotaInfoList'] = []
        if self.quota_info_list is not None:
            for k1 in self.quota_info_list:
                result['quotaInfoList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('data') is not None:
            temp_model = main_models.ListQuotasResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('marker') is not None:
            self.marker = m.get('marker')

        if m.get('maxItem') is not None:
            self.max_item = m.get('maxItem')

        self.quota_info_list = []
        if m.get('quotaInfoList') is not None:
            for k1 in m.get('quotaInfoList'):
                temp_model = main_models.ListQuotasResponseBodyQuotaInfoList()
                self.quota_info_list.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListQuotasResponseBodyQuotaInfoList(DaraModel):
    def __init__(
        self,
        tags: List[main_models.ListQuotasResponseBodyQuotaInfoListTags] = None,
        billing_policy: main_models.ListQuotasResponseBodyQuotaInfoListBillingPolicy = None,
        cluster: str = None,
        create_time: int = None,
        creator_id: str = None,
        id: str = None,
        name: str = None,
        nick_name: str = None,
        parameter: Dict[str, Any] = None,
        parent_id: str = None,
        region_id: str = None,
        sale_tag: main_models.ListQuotasResponseBodyQuotaInfoListSaleTag = None,
        schedule_info: main_models.ListQuotasResponseBodyQuotaInfoListScheduleInfo = None,
        status: str = None,
        sub_quota_info_list: List[main_models.ListQuotasResponseBodyQuotaInfoListSubQuotaInfoList] = None,
        tag: str = None,
        tenant_id: str = None,
        type: str = None,
        version: str = None,
    ):
        # The tags.
        self.tags = tags
        # The billing information.
        self.billing_policy = billing_policy
        # The ID of the cluster.
        self.cluster = cluster
        # The time when the quota was created.
        self.create_time = create_time
        # The ID of the account that created the quota. This ID is an Alibaba Cloud account UID.
        self.creator_id = creator_id
        # The ID of the quota.
        self.id = id
        # The name of the quota.
        self.name = name
        # The alias of the quota.
        self.nick_name = nick_name
        # The parameters of the quota.
        self.parameter = parameter
        # The ID of the parent resource.
        self.parent_id = parent_id
        # The ID of the region.
        self.region_id = region_id
        # The sales tag of the quota. This tag is the same as the billing identifier and is used for cost allocation.
        self.sale_tag = sale_tag
        # The time-based scheduling information.
        self.schedule_info = schedule_info
        # The status of the quota.
        self.status = status
        # The information about the sub-quotas.
        self.sub_quota_info_list = sub_quota_info_list
        # The tag of the quota.
        self.tag = tag
        # The ID of the tenant.
        self.tenant_id = tenant_id
        # The type of the resource system. This parameter corresponds to the resourceSystemType parameter of the control cluster.
        self.type = type
        # The version number.
        self.version = version

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
        if self.billing_policy:
            self.billing_policy.validate()
        if self.sale_tag:
            self.sale_tag.validate()
        if self.schedule_info:
            self.schedule_info.validate()
        if self.sub_quota_info_list:
            for v1 in self.sub_quota_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.billing_policy is not None:
            result['billingPolicy'] = self.billing_policy.to_map()

        if self.cluster is not None:
            result['cluster'] = self.cluster

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.creator_id is not None:
            result['creatorId'] = self.creator_id

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.nick_name is not None:
            result['nickName'] = self.nick_name

        if self.parameter is not None:
            result['parameter'] = self.parameter

        if self.parent_id is not None:
            result['parentId'] = self.parent_id

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.sale_tag is not None:
            result['saleTag'] = self.sale_tag.to_map()

        if self.schedule_info is not None:
            result['scheduleInfo'] = self.schedule_info.to_map()

        if self.status is not None:
            result['status'] = self.status

        result['subQuotaInfoList'] = []
        if self.sub_quota_info_list is not None:
            for k1 in self.sub_quota_info_list:
                result['subQuotaInfoList'].append(k1.to_map() if k1 else None)

        if self.tag is not None:
            result['tag'] = self.tag

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.type is not None:
            result['type'] = self.type

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListQuotasResponseBodyQuotaInfoListTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('billingPolicy') is not None:
            temp_model = main_models.ListQuotasResponseBodyQuotaInfoListBillingPolicy()
            self.billing_policy = temp_model.from_map(m.get('billingPolicy'))

        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')

        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')

        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('saleTag') is not None:
            temp_model = main_models.ListQuotasResponseBodyQuotaInfoListSaleTag()
            self.sale_tag = temp_model.from_map(m.get('saleTag'))

        if m.get('scheduleInfo') is not None:
            temp_model = main_models.ListQuotasResponseBodyQuotaInfoListScheduleInfo()
            self.schedule_info = temp_model.from_map(m.get('scheduleInfo'))

        if m.get('status') is not None:
            self.status = m.get('status')

        self.sub_quota_info_list = []
        if m.get('subQuotaInfoList') is not None:
            for k1 in m.get('subQuotaInfoList'):
                temp_model = main_models.ListQuotasResponseBodyQuotaInfoListSubQuotaInfoList()
                self.sub_quota_info_list.append(temp_model.from_map(k1))

        if m.get('tag') is not None:
            self.tag = m.get('tag')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class ListQuotasResponseBodyQuotaInfoListSubQuotaInfoList(DaraModel):
    def __init__(
        self,
        billing_policy: main_models.ListQuotasResponseBodyQuotaInfoListSubQuotaInfoListBillingPolicy = None,
        cluster: str = None,
        create_time: int = None,
        creator_id: str = None,
        id: str = None,
        name: str = None,
        nick_name: str = None,
        parameter: main_models.ListQuotasResponseBodyQuotaInfoListSubQuotaInfoListParameter = None,
        parent_id: str = None,
        region_id: str = None,
        sale_tag: main_models.ListQuotasResponseBodyQuotaInfoListSubQuotaInfoListSaleTag = None,
        schedule_info: main_models.ListQuotasResponseBodyQuotaInfoListSubQuotaInfoListScheduleInfo = None,
        status: str = None,
        tag: str = None,
        tenant_id: str = None,
        type: str = None,
        version: str = None,
    ):
        # The billing information.
        self.billing_policy = billing_policy
        # The ID of the cluster.
        self.cluster = cluster
        # The time when the quota was created.
        self.create_time = create_time
        # The ID of the account that created the quota. This ID is an Alibaba Cloud account UID.
        self.creator_id = creator_id
        # The ID of the sub-quota.
        self.id = id
        # The name of the sub-quota.
        self.name = name
        # The alias of the sub-quota.
        self.nick_name = nick_name
        # The quota description.
        self.parameter = parameter
        # The ID of the parent resource.
        self.parent_id = parent_id
        # The ID of the region.
        self.region_id = region_id
        # The sales tag of the quota. This tag is the same as the billing identifier and is used for cost allocation.
        self.sale_tag = sale_tag
        # The time-based scheduling information.
        self.schedule_info = schedule_info
        # The status of the quota.
        self.status = status
        # The tag of the quota.
        self.tag = tag
        # The ID of the tenant.
        self.tenant_id = tenant_id
        # The type of the resource system. This parameter corresponds to the resourceSystemType parameter of the control cluster.
        self.type = type
        # The version number.
        self.version = version

    def validate(self):
        if self.billing_policy:
            self.billing_policy.validate()
        if self.parameter:
            self.parameter.validate()
        if self.sale_tag:
            self.sale_tag.validate()
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.billing_policy is not None:
            result['billingPolicy'] = self.billing_policy.to_map()

        if self.cluster is not None:
            result['cluster'] = self.cluster

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.creator_id is not None:
            result['creatorId'] = self.creator_id

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.nick_name is not None:
            result['nickName'] = self.nick_name

        if self.parameter is not None:
            result['parameter'] = self.parameter.to_map()

        if self.parent_id is not None:
            result['parentId'] = self.parent_id

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.sale_tag is not None:
            result['saleTag'] = self.sale_tag.to_map()

        if self.schedule_info is not None:
            result['scheduleInfo'] = self.schedule_info.to_map()

        if self.status is not None:
            result['status'] = self.status

        if self.tag is not None:
            result['tag'] = self.tag

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.type is not None:
            result['type'] = self.type

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingPolicy') is not None:
            temp_model = main_models.ListQuotasResponseBodyQuotaInfoListSubQuotaInfoListBillingPolicy()
            self.billing_policy = temp_model.from_map(m.get('billingPolicy'))

        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')

        if m.get('parameter') is not None:
            temp_model = main_models.ListQuotasResponseBodyQuotaInfoListSubQuotaInfoListParameter()
            self.parameter = temp_model.from_map(m.get('parameter'))

        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('saleTag') is not None:
            temp_model = main_models.ListQuotasResponseBodyQuotaInfoListSubQuotaInfoListSaleTag()
            self.sale_tag = temp_model.from_map(m.get('saleTag'))

        if m.get('scheduleInfo') is not None:
            temp_model = main_models.ListQuotasResponseBodyQuotaInfoListSubQuotaInfoListScheduleInfo()
            self.schedule_info = temp_model.from_map(m.get('scheduleInfo'))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('tag') is not None:
            self.tag = m.get('tag')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class ListQuotasResponseBodyQuotaInfoListSubQuotaInfoListScheduleInfo(DaraModel):
    def __init__(
        self,
        curr_plan: str = None,
        curr_time: str = None,
        next_plan: str = None,
        next_time: str = None,
        once_plan: str = None,
        once_time: str = None,
        operator_name: str = None,
        timezone: str = None,
    ):
        # The quota plan that is currently in effect.
        self.curr_plan = curr_plan
        # The time when the current plan took effect.
        self.curr_time = curr_time
        # The next quota plan that is scheduled to take effect.
        self.next_plan = next_plan
        # The time when the next plan is scheduled to take effect.
        self.next_time = next_time
        # The quota plan that takes effect immediately. This parameter is returned only when a user triggers an immediate plan that is different from the current plan.
        self.once_plan = once_plan
        # The time when the immediate plan was triggered.
        self.once_time = once_time
        # The name of the operator.
        self.operator_name = operator_name
        # The time zone.
        self.timezone = timezone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.curr_plan is not None:
            result['currPlan'] = self.curr_plan

        if self.curr_time is not None:
            result['currTime'] = self.curr_time

        if self.next_plan is not None:
            result['nextPlan'] = self.next_plan

        if self.next_time is not None:
            result['nextTime'] = self.next_time

        if self.once_plan is not None:
            result['oncePlan'] = self.once_plan

        if self.once_time is not None:
            result['onceTime'] = self.once_time

        if self.operator_name is not None:
            result['operatorName'] = self.operator_name

        if self.timezone is not None:
            result['timezone'] = self.timezone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currPlan') is not None:
            self.curr_plan = m.get('currPlan')

        if m.get('currTime') is not None:
            self.curr_time = m.get('currTime')

        if m.get('nextPlan') is not None:
            self.next_plan = m.get('nextPlan')

        if m.get('nextTime') is not None:
            self.next_time = m.get('nextTime')

        if m.get('oncePlan') is not None:
            self.once_plan = m.get('oncePlan')

        if m.get('onceTime') is not None:
            self.once_time = m.get('onceTime')

        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')

        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')

        return self

class ListQuotasResponseBodyQuotaInfoListSubQuotaInfoListSaleTag(DaraModel):
    def __init__(
        self,
        resource_ids: List[str] = None,
        resource_type: str = None,
    ):
        # The IDs of the resources. This ID is also used in the billing system. You can use this ID to associate the costs of a quota with a tag.
        self.resource_ids = resource_ids
        # The type of the resource. Valid values: quota and project.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        return self

class ListQuotasResponseBodyQuotaInfoListSubQuotaInfoListParameter(DaraModel):
    def __init__(
        self,
        adhoc_slot: int = None,
        auto_scale_cpulimit: int = None,
        elastic_reserved_cu: int = None,
        enable_priority: bool = None,
        force_reserved_min: bool = None,
        max_cu: int = None,
        max_gu: int = None,
        min_cu: int = None,
        min_gu: int = None,
        scheduler_type: str = None,
        single_job_culimit: int = None,
        slot_num: int = None,
    ):
        self.adhoc_slot = adhoc_slot
        self.auto_scale_cpulimit = auto_scale_cpulimit
        # The elastically reserved CUs.
        self.elastic_reserved_cu = elastic_reserved_cu
        # Indicates whether to enable priority-based scheduling.
        self.enable_priority = enable_priority
        # Indicates whether the resource is exclusive.
        self.force_reserved_min = force_reserved_min
        # The maximum reserved computing units (CUs).
        # 
        # This parameter is required.
        self.max_cu = max_cu
        self.max_gu = max_gu
        # The minimum reserved CUs.
        # 
        # This parameter is required.
        self.min_cu = min_cu
        self.min_gu = min_gu
        # The scheduling policy.
        self.scheduler_type = scheduler_type
        # The maximum CUs for a single job.
        self.single_job_culimit = single_job_culimit
        self.slot_num = slot_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adhoc_slot is not None:
            result['adhocSlot'] = self.adhoc_slot

        if self.auto_scale_cpulimit is not None:
            result['autoScaleCPULimit'] = self.auto_scale_cpulimit

        if self.elastic_reserved_cu is not None:
            result['elasticReservedCU'] = self.elastic_reserved_cu

        if self.enable_priority is not None:
            result['enablePriority'] = self.enable_priority

        if self.force_reserved_min is not None:
            result['forceReservedMin'] = self.force_reserved_min

        if self.max_cu is not None:
            result['maxCU'] = self.max_cu

        if self.max_gu is not None:
            result['maxGu'] = self.max_gu

        if self.min_cu is not None:
            result['minCU'] = self.min_cu

        if self.min_gu is not None:
            result['minGu'] = self.min_gu

        if self.scheduler_type is not None:
            result['schedulerType'] = self.scheduler_type

        if self.single_job_culimit is not None:
            result['singleJobCULimit'] = self.single_job_culimit

        if self.slot_num is not None:
            result['slotNum'] = self.slot_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('adhocSlot') is not None:
            self.adhoc_slot = m.get('adhocSlot')

        if m.get('autoScaleCPULimit') is not None:
            self.auto_scale_cpulimit = m.get('autoScaleCPULimit')

        if m.get('elasticReservedCU') is not None:
            self.elastic_reserved_cu = m.get('elasticReservedCU')

        if m.get('enablePriority') is not None:
            self.enable_priority = m.get('enablePriority')

        if m.get('forceReservedMin') is not None:
            self.force_reserved_min = m.get('forceReservedMin')

        if m.get('maxCU') is not None:
            self.max_cu = m.get('maxCU')

        if m.get('maxGu') is not None:
            self.max_gu = m.get('maxGu')

        if m.get('minCU') is not None:
            self.min_cu = m.get('minCU')

        if m.get('minGu') is not None:
            self.min_gu = m.get('minGu')

        if m.get('schedulerType') is not None:
            self.scheduler_type = m.get('schedulerType')

        if m.get('singleJobCULimit') is not None:
            self.single_job_culimit = m.get('singleJobCULimit')

        if m.get('slotNum') is not None:
            self.slot_num = m.get('slotNum')

        return self

class ListQuotasResponseBodyQuotaInfoListSubQuotaInfoListBillingPolicy(DaraModel):
    def __init__(
        self,
        billing_method: str = None,
        odps_spec_code: str = None,
        order_id: str = None,
    ):
        # The billing method.
        # 
        # - subscription: The subscription billing method.
        # 
        # - payasyougo: The pay-as-you-go billing method.
        self.billing_method = billing_method
        # The specifications of the order.
        self.odps_spec_code = odps_spec_code
        # The ID of the order.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method

        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code

        if self.order_id is not None:
            result['orderId'] = self.order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')

        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')

        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')

        return self

class ListQuotasResponseBodyQuotaInfoListScheduleInfo(DaraModel):
    def __init__(
        self,
        curr_plan: str = None,
        curr_time: str = None,
        next_plan: str = None,
        next_time: str = None,
        once_plan: str = None,
        once_time: str = None,
        operator_name: str = None,
        timezone: str = None,
    ):
        # The quota plan that is currently in effect.
        self.curr_plan = curr_plan
        # The time when the current plan took effect.
        self.curr_time = curr_time
        # The next quota plan that is scheduled to take effect.
        self.next_plan = next_plan
        # The time when the next plan is scheduled to take effect.
        self.next_time = next_time
        # The quota plan that takes effect immediately. This parameter is returned only when a user triggers an immediate plan that is different from the current plan.
        self.once_plan = once_plan
        # The time when the immediate plan was triggered.
        self.once_time = once_time
        # The name of the operator.
        self.operator_name = operator_name
        # The time zone.
        self.timezone = timezone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.curr_plan is not None:
            result['currPlan'] = self.curr_plan

        if self.curr_time is not None:
            result['currTime'] = self.curr_time

        if self.next_plan is not None:
            result['nextPlan'] = self.next_plan

        if self.next_time is not None:
            result['nextTime'] = self.next_time

        if self.once_plan is not None:
            result['oncePlan'] = self.once_plan

        if self.once_time is not None:
            result['onceTime'] = self.once_time

        if self.operator_name is not None:
            result['operatorName'] = self.operator_name

        if self.timezone is not None:
            result['timezone'] = self.timezone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currPlan') is not None:
            self.curr_plan = m.get('currPlan')

        if m.get('currTime') is not None:
            self.curr_time = m.get('currTime')

        if m.get('nextPlan') is not None:
            self.next_plan = m.get('nextPlan')

        if m.get('nextTime') is not None:
            self.next_time = m.get('nextTime')

        if m.get('oncePlan') is not None:
            self.once_plan = m.get('oncePlan')

        if m.get('onceTime') is not None:
            self.once_time = m.get('onceTime')

        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')

        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')

        return self

class ListQuotasResponseBodyQuotaInfoListSaleTag(DaraModel):
    def __init__(
        self,
        resource_ids: List[str] = None,
        resource_type: str = None,
    ):
        # The IDs of the resources. This ID is also used in the billing system. You can use this ID to associate the costs of a quota with a tag.
        self.resource_ids = resource_ids
        # The type of the resource. Valid values: quota and project.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        return self

class ListQuotasResponseBodyQuotaInfoListBillingPolicy(DaraModel):
    def __init__(
        self,
        billing_method: str = None,
        odps_spec_code: str = None,
        order_id: str = None,
    ):
        # The billing method.
        # 
        # - subscription: The subscription billing method.
        # 
        # - payasyougo: The pay-as-you-go billing method.
        self.billing_method = billing_method
        # The specifications of the order.
        self.odps_spec_code = odps_spec_code
        # The ID of the order.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method

        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code

        if self.order_id is not None:
            result['orderId'] = self.order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')

        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')

        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')

        return self

class ListQuotasResponseBodyQuotaInfoListTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The key of the tag.
        self.tag_key = tag_key
        # The value of the tag.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class ListQuotasResponseBodyData(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        marker: str = None,
        max_item: int = None,
        quota_info_list: List[main_models.ListQuotasResponseBodyDataQuotaInfoList] = None,
    ):
        # The token for the next page of results. If this parameter has a value, more results are available. To get the next page, include this value in the \\`NextToken\\` parameter of the next request.
        self.next_token = next_token
        # The results are returned in alphabetical order, starting from the entry after the marker.
        self.marker = marker
        # The maximum number of entries returned per page.
        self.max_item = max_item
        # The list of quotas.
        self.quota_info_list = quota_info_list

    def validate(self):
        if self.quota_info_list:
            for v1 in self.quota_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.marker is not None:
            result['marker'] = self.marker

        if self.max_item is not None:
            result['maxItem'] = self.max_item

        result['quotaInfoList'] = []
        if self.quota_info_list is not None:
            for k1 in self.quota_info_list:
                result['quotaInfoList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('marker') is not None:
            self.marker = m.get('marker')

        if m.get('maxItem') is not None:
            self.max_item = m.get('maxItem')

        self.quota_info_list = []
        if m.get('quotaInfoList') is not None:
            for k1 in m.get('quotaInfoList'):
                temp_model = main_models.ListQuotasResponseBodyDataQuotaInfoList()
                self.quota_info_list.append(temp_model.from_map(k1))

        return self

class ListQuotasResponseBodyDataQuotaInfoList(DaraModel):
    def __init__(
        self,
        tags: List[main_models.ListQuotasResponseBodyDataQuotaInfoListTags] = None,
        billing_policy: main_models.ListQuotasResponseBodyDataQuotaInfoListBillingPolicy = None,
        cluster: str = None,
        create_time: int = None,
        creator_id: str = None,
        id: str = None,
        name: str = None,
        nick_name: str = None,
        parameter: Dict[str, Any] = None,
        parent_id: str = None,
        region_id: str = None,
        sale_tag: main_models.ListQuotasResponseBodyDataQuotaInfoListSaleTag = None,
        schedule_info: main_models.ListQuotasResponseBodyDataQuotaInfoListScheduleInfo = None,
        status: str = None,
        sub_quota_info_list: List[main_models.ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoList] = None,
        tag: str = None,
        tenant_id: str = None,
        type: str = None,
        version: str = None,
    ):
        # The tags.
        self.tags = tags
        # The billing information.
        self.billing_policy = billing_policy
        # The ID of the cluster.
        self.cluster = cluster
        # The time when the quota was created.
        self.create_time = create_time
        # The ID of the account that created the quota. This ID is an Alibaba Cloud account UID.
        self.creator_id = creator_id
        # The ID of the quota.
        self.id = id
        # The name of the quota.
        self.name = name
        # The alias of the quota.
        self.nick_name = nick_name
        # The quota description.
        self.parameter = parameter
        # The ID of the parent resource.
        self.parent_id = parent_id
        # The ID of the region.
        self.region_id = region_id
        # The sales tag of the quota. This tag is the same as the billing identifier and is used for cost allocation.
        self.sale_tag = sale_tag
        # The time-based scheduling information.
        self.schedule_info = schedule_info
        # The status of the quota.
        self.status = status
        # The information about the sub-quotas.
        self.sub_quota_info_list = sub_quota_info_list
        # The tag of the quota.
        self.tag = tag
        # The ID of the tenant.
        self.tenant_id = tenant_id
        # The type of the resource system. This parameter corresponds to the resourceSystemType parameter of the control cluster.
        self.type = type
        # The version number.
        self.version = version

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
        if self.billing_policy:
            self.billing_policy.validate()
        if self.sale_tag:
            self.sale_tag.validate()
        if self.schedule_info:
            self.schedule_info.validate()
        if self.sub_quota_info_list:
            for v1 in self.sub_quota_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.billing_policy is not None:
            result['billingPolicy'] = self.billing_policy.to_map()

        if self.cluster is not None:
            result['cluster'] = self.cluster

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.creator_id is not None:
            result['creatorId'] = self.creator_id

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.nick_name is not None:
            result['nickName'] = self.nick_name

        if self.parameter is not None:
            result['parameter'] = self.parameter

        if self.parent_id is not None:
            result['parentId'] = self.parent_id

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.sale_tag is not None:
            result['saleTag'] = self.sale_tag.to_map()

        if self.schedule_info is not None:
            result['scheduleInfo'] = self.schedule_info.to_map()

        if self.status is not None:
            result['status'] = self.status

        result['subQuotaInfoList'] = []
        if self.sub_quota_info_list is not None:
            for k1 in self.sub_quota_info_list:
                result['subQuotaInfoList'].append(k1.to_map() if k1 else None)

        if self.tag is not None:
            result['tag'] = self.tag

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.type is not None:
            result['type'] = self.type

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListQuotasResponseBodyDataQuotaInfoListTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('billingPolicy') is not None:
            temp_model = main_models.ListQuotasResponseBodyDataQuotaInfoListBillingPolicy()
            self.billing_policy = temp_model.from_map(m.get('billingPolicy'))

        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')

        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')

        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('saleTag') is not None:
            temp_model = main_models.ListQuotasResponseBodyDataQuotaInfoListSaleTag()
            self.sale_tag = temp_model.from_map(m.get('saleTag'))

        if m.get('scheduleInfo') is not None:
            temp_model = main_models.ListQuotasResponseBodyDataQuotaInfoListScheduleInfo()
            self.schedule_info = temp_model.from_map(m.get('scheduleInfo'))

        if m.get('status') is not None:
            self.status = m.get('status')

        self.sub_quota_info_list = []
        if m.get('subQuotaInfoList') is not None:
            for k1 in m.get('subQuotaInfoList'):
                temp_model = main_models.ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoList()
                self.sub_quota_info_list.append(temp_model.from_map(k1))

        if m.get('tag') is not None:
            self.tag = m.get('tag')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoList(DaraModel):
    def __init__(
        self,
        billing_policy: main_models.ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoListBillingPolicy = None,
        cluster: str = None,
        create_time: int = None,
        creator_id: str = None,
        id: str = None,
        name: str = None,
        nick_name: str = None,
        parameter: main_models.ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoListParameter = None,
        parent_id: str = None,
        region_id: str = None,
        sale_tag: main_models.ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoListSaleTag = None,
        schedule_info: main_models.ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoListScheduleInfo = None,
        status: str = None,
        tag: str = None,
        tenant_id: str = None,
        type: str = None,
        version: str = None,
    ):
        # The billing information.
        self.billing_policy = billing_policy
        # The ID of the cluster.
        self.cluster = cluster
        # The time when the resource was created.
        self.create_time = create_time
        # The creator of the resource. This is the UID of an Alibaba Cloud account.
        self.creator_id = creator_id
        # The ID of the sub-quota.
        self.id = id
        # The name of the sub-quota.
        self.name = name
        # The alias of the sub-quota.
        self.nick_name = nick_name
        # The description of the quota.
        self.parameter = parameter
        # The ID of the parent resource.
        self.parent_id = parent_id
        # The ID of the region.
        self.region_id = region_id
        # The identifier of the MaxCompute quota object. This identifier is the same as the one in the Alibaba Cloud bill and is used in tagging scenarios.
        self.sale_tag = sale_tag
        # The time-based scheduling information.
        self.schedule_info = schedule_info
        # The status of the quota.
        self.status = status
        # The resource tag of the quota.
        self.tag = tag
        # The ID of the tenant.
        self.tenant_id = tenant_id
        # The type of the resource system. This parameter corresponds to the resourceSystemType parameter of the control cluster.
        self.type = type
        # The version number.
        self.version = version

    def validate(self):
        if self.billing_policy:
            self.billing_policy.validate()
        if self.parameter:
            self.parameter.validate()
        if self.sale_tag:
            self.sale_tag.validate()
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.billing_policy is not None:
            result['billingPolicy'] = self.billing_policy.to_map()

        if self.cluster is not None:
            result['cluster'] = self.cluster

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.creator_id is not None:
            result['creatorId'] = self.creator_id

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.nick_name is not None:
            result['nickName'] = self.nick_name

        if self.parameter is not None:
            result['parameter'] = self.parameter.to_map()

        if self.parent_id is not None:
            result['parentId'] = self.parent_id

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.sale_tag is not None:
            result['saleTag'] = self.sale_tag.to_map()

        if self.schedule_info is not None:
            result['scheduleInfo'] = self.schedule_info.to_map()

        if self.status is not None:
            result['status'] = self.status

        if self.tag is not None:
            result['tag'] = self.tag

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.type is not None:
            result['type'] = self.type

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingPolicy') is not None:
            temp_model = main_models.ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoListBillingPolicy()
            self.billing_policy = temp_model.from_map(m.get('billingPolicy'))

        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')

        if m.get('parameter') is not None:
            temp_model = main_models.ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoListParameter()
            self.parameter = temp_model.from_map(m.get('parameter'))

        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('saleTag') is not None:
            temp_model = main_models.ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoListSaleTag()
            self.sale_tag = temp_model.from_map(m.get('saleTag'))

        if m.get('scheduleInfo') is not None:
            temp_model = main_models.ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoListScheduleInfo()
            self.schedule_info = temp_model.from_map(m.get('scheduleInfo'))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('tag') is not None:
            self.tag = m.get('tag')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoListScheduleInfo(DaraModel):
    def __init__(
        self,
        curr_plan: str = None,
        curr_time: str = None,
        next_plan: str = None,
        next_time: str = None,
        once_plan: str = None,
        once_time: str = None,
        operator_name: str = None,
        timezone: str = None,
    ):
        # The quota plan that is currently in effect.
        self.curr_plan = curr_plan
        # The time when the current plan took effect.
        self.curr_time = curr_time
        # The next quota plan that is scheduled to take effect.
        self.next_plan = next_plan
        # The time when the next plan is scheduled to take effect.
        self.next_time = next_time
        # The quota plan that takes effect immediately. This parameter is returned only if a user triggers an immediate plan that is different from `currPlan`.
        self.once_plan = once_plan
        # The time when the immediate-effect plan was triggered.
        self.once_time = once_time
        # The name of the operator.
        self.operator_name = operator_name
        # The time zone.
        self.timezone = timezone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.curr_plan is not None:
            result['currPlan'] = self.curr_plan

        if self.curr_time is not None:
            result['currTime'] = self.curr_time

        if self.next_plan is not None:
            result['nextPlan'] = self.next_plan

        if self.next_time is not None:
            result['nextTime'] = self.next_time

        if self.once_plan is not None:
            result['oncePlan'] = self.once_plan

        if self.once_time is not None:
            result['onceTime'] = self.once_time

        if self.operator_name is not None:
            result['operatorName'] = self.operator_name

        if self.timezone is not None:
            result['timezone'] = self.timezone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currPlan') is not None:
            self.curr_plan = m.get('currPlan')

        if m.get('currTime') is not None:
            self.curr_time = m.get('currTime')

        if m.get('nextPlan') is not None:
            self.next_plan = m.get('nextPlan')

        if m.get('nextTime') is not None:
            self.next_time = m.get('nextTime')

        if m.get('oncePlan') is not None:
            self.once_plan = m.get('oncePlan')

        if m.get('onceTime') is not None:
            self.once_time = m.get('onceTime')

        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')

        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')

        return self

class ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoListSaleTag(DaraModel):
    def __init__(
        self,
        resource_ids: List[str] = None,
        resource_type: str = None,
    ):
        # The identifier of the MaxCompute quota object. This identifier also exists in the Alibaba Cloud sales subsystem. It associates the costs of the quota object with a tag.
        self.resource_ids = resource_ids
        # The type of the object. Only \\`quota\\` and \\`project\\` are supported.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        return self

class ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoListParameter(DaraModel):
    def __init__(
        self,
        adhoc_slot: int = None,
        auto_scale_cpulimit: int = None,
        elastic_reserved_cu: int = None,
        enable_priority: bool = None,
        force_reserved_min: bool = None,
        max_cu: int = None,
        max_gu: int = None,
        min_cu: int = None,
        min_gu: int = None,
        scheduler_type: str = None,
        single_job_culimit: int = None,
        slot_num: int = None,
    ):
        self.adhoc_slot = adhoc_slot
        self.auto_scale_cpulimit = auto_scale_cpulimit
        # The value of elastically reserved CUs.
        self.elastic_reserved_cu = elastic_reserved_cu
        # Specifies whether to enable priority-based scheduling.
        self.enable_priority = enable_priority
        # Specifies whether the resource is exclusive.
        self.force_reserved_min = force_reserved_min
        # The upper limit of reserved CUs.
        # 
        # This parameter is required.
        self.max_cu = max_cu
        self.max_gu = max_gu
        # The minimum number of guaranteed reserved CUs.
        # 
        # This parameter is required.
        self.min_cu = min_cu
        self.min_gu = min_gu
        # The scheduling policy.
        self.scheduler_type = scheduler_type
        # The upper limit of CUs for a single job.
        self.single_job_culimit = single_job_culimit
        self.slot_num = slot_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adhoc_slot is not None:
            result['adhocSlot'] = self.adhoc_slot

        if self.auto_scale_cpulimit is not None:
            result['autoScaleCPULimit'] = self.auto_scale_cpulimit

        if self.elastic_reserved_cu is not None:
            result['elasticReservedCU'] = self.elastic_reserved_cu

        if self.enable_priority is not None:
            result['enablePriority'] = self.enable_priority

        if self.force_reserved_min is not None:
            result['forceReservedMin'] = self.force_reserved_min

        if self.max_cu is not None:
            result['maxCU'] = self.max_cu

        if self.max_gu is not None:
            result['maxGu'] = self.max_gu

        if self.min_cu is not None:
            result['minCU'] = self.min_cu

        if self.min_gu is not None:
            result['minGu'] = self.min_gu

        if self.scheduler_type is not None:
            result['schedulerType'] = self.scheduler_type

        if self.single_job_culimit is not None:
            result['singleJobCULimit'] = self.single_job_culimit

        if self.slot_num is not None:
            result['slotNum'] = self.slot_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('adhocSlot') is not None:
            self.adhoc_slot = m.get('adhocSlot')

        if m.get('autoScaleCPULimit') is not None:
            self.auto_scale_cpulimit = m.get('autoScaleCPULimit')

        if m.get('elasticReservedCU') is not None:
            self.elastic_reserved_cu = m.get('elasticReservedCU')

        if m.get('enablePriority') is not None:
            self.enable_priority = m.get('enablePriority')

        if m.get('forceReservedMin') is not None:
            self.force_reserved_min = m.get('forceReservedMin')

        if m.get('maxCU') is not None:
            self.max_cu = m.get('maxCU')

        if m.get('maxGu') is not None:
            self.max_gu = m.get('maxGu')

        if m.get('minCU') is not None:
            self.min_cu = m.get('minCU')

        if m.get('minGu') is not None:
            self.min_gu = m.get('minGu')

        if m.get('schedulerType') is not None:
            self.scheduler_type = m.get('schedulerType')

        if m.get('singleJobCULimit') is not None:
            self.single_job_culimit = m.get('singleJobCULimit')

        if m.get('slotNum') is not None:
            self.slot_num = m.get('slotNum')

        return self

class ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoListBillingPolicy(DaraModel):
    def __init__(
        self,
        billing_method: str = None,
        odps_spec_code: str = None,
        order_id: str = None,
    ):
        # The billing method.
        # 
        # - subscription: The subscription billing method.
        # 
        # - payasyougo: The pay-as-you-go billing method.
        self.billing_method = billing_method
        # The specifications of the order.
        self.odps_spec_code = odps_spec_code
        # The ID of the order.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method

        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code

        if self.order_id is not None:
            result['orderId'] = self.order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')

        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')

        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')

        return self

class ListQuotasResponseBodyDataQuotaInfoListScheduleInfo(DaraModel):
    def __init__(
        self,
        curr_plan: str = None,
        curr_time: str = None,
        next_plan: str = None,
        next_time: str = None,
        once_plan: str = None,
        once_time: str = None,
        operator_name: str = None,
        timezone: str = None,
    ):
        # The quota plan that is currently in effect.
        self.curr_plan = curr_plan
        # The time when the current plan took effect.
        self.curr_time = curr_time
        # The next quota plan that is scheduled to take effect.
        self.next_plan = next_plan
        # The time when the next plan is scheduled to take effect.
        self.next_time = next_time
        # The quota plan that takes effect immediately. This parameter is returned only when a user triggers an immediate plan that is different from the current plan.
        self.once_plan = once_plan
        # The time when the immediate plan was triggered.
        self.once_time = once_time
        # The name of the operator.
        self.operator_name = operator_name
        # The time zone.
        self.timezone = timezone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.curr_plan is not None:
            result['currPlan'] = self.curr_plan

        if self.curr_time is not None:
            result['currTime'] = self.curr_time

        if self.next_plan is not None:
            result['nextPlan'] = self.next_plan

        if self.next_time is not None:
            result['nextTime'] = self.next_time

        if self.once_plan is not None:
            result['oncePlan'] = self.once_plan

        if self.once_time is not None:
            result['onceTime'] = self.once_time

        if self.operator_name is not None:
            result['operatorName'] = self.operator_name

        if self.timezone is not None:
            result['timezone'] = self.timezone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currPlan') is not None:
            self.curr_plan = m.get('currPlan')

        if m.get('currTime') is not None:
            self.curr_time = m.get('currTime')

        if m.get('nextPlan') is not None:
            self.next_plan = m.get('nextPlan')

        if m.get('nextTime') is not None:
            self.next_time = m.get('nextTime')

        if m.get('oncePlan') is not None:
            self.once_plan = m.get('oncePlan')

        if m.get('onceTime') is not None:
            self.once_time = m.get('onceTime')

        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')

        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')

        return self

class ListQuotasResponseBodyDataQuotaInfoListSaleTag(DaraModel):
    def __init__(
        self,
        resource_ids: List[str] = None,
        resource_type: str = None,
    ):
        # The IDs of the resources. This ID is also used in the billing system. You can use this ID to associate the costs of a quota with a tag.
        self.resource_ids = resource_ids
        # The type of the resource. Valid values: quota and project.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        return self

class ListQuotasResponseBodyDataQuotaInfoListBillingPolicy(DaraModel):
    def __init__(
        self,
        billing_method: str = None,
        odps_spec_code: str = None,
        order_id: str = None,
    ):
        # The billing method.
        # 
        # - subscription: The subscription billing method.
        # 
        # - payasyougo: The pay-as-you-go billing method.
        self.billing_method = billing_method
        # The specifications of the order.
        self.odps_spec_code = odps_spec_code
        # The ID of the order.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method

        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code

        if self.order_id is not None:
            result['orderId'] = self.order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')

        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')

        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')

        return self

class ListQuotasResponseBodyDataQuotaInfoListTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

