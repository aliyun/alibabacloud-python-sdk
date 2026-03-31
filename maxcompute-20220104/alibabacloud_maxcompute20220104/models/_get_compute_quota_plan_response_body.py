# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class GetComputeQuotaPlanResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetComputeQuotaPlanResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The HTTP status code.
        # 
        # - 1xx: informational response. The request is received and is being processed.
        # - 2xx: success. The request is successfully received, understood, and accepted by the server.
        # - 3xx: redirection. The request is redirected, and further actions are required to complete the request.
        # - 4xx: client error. The request contains invalid request parameters or syntaxes, or specific request conditions cannot be met.
        # - 5xx: server error. The server cannot meet requirements due to other reasons.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg

        if self.http_code is not None:
            result['httpCode'] = self.http_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetComputeQuotaPlanResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')

        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetComputeQuotaPlanResponseBodyData(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        is_effective: bool = None,
        name: str = None,
        quota: main_models.GetComputeQuotaPlanResponseBodyDataQuota = None,
    ):
        # The time when the quota plan was created.
        self.create_time = create_time
        # Whether it is currently effective.
        # > 
        # > - A Quota plan that has taken effect cannot be deleted, i.e., isEffective=true
        self.is_effective = is_effective
        # The name of the quota plan.
        self.name = name
        # The details of the quota.
        self.quota = quota

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.is_effective is not None:
            result['isEffective'] = self.is_effective

        if self.name is not None:
            result['name'] = self.name

        if self.quota is not None:
            result['quota'] = self.quota.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('isEffective') is not None:
            self.is_effective = m.get('isEffective')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('quota') is not None:
            temp_model = main_models.GetComputeQuotaPlanResponseBodyDataQuota()
            self.quota = temp_model.from_map(m.get('quota'))

        return self

class GetComputeQuotaPlanResponseBodyDataQuota(DaraModel):
    def __init__(
        self,
        cluster: str = None,
        create_time: int = None,
        creator_id: str = None,
        id: str = None,
        name: str = None,
        nick_name: str = None,
        parameter: main_models.GetComputeQuotaPlanResponseBodyDataQuotaParameter = None,
        region_id: str = None,
        status: str = None,
        sub_quota_info_list: List[main_models.GetComputeQuotaPlanResponseBodyDataQuotaSubQuotaInfoList] = None,
        tenant_id: str = None,
        type: str = None,
        version: str = None,
    ):
        # Cluster ID.
        self.cluster = cluster
        # Creation time.
        self.create_time = create_time
        # Creator\\"s cloud account UID.
        self.creator_id = creator_id
        # The ID of the level-1 quota.
        self.id = id
        # The name of the level-1 quota.
        self.name = name
        # The nickname of the level-1 quota.
        self.nick_name = nick_name
        # CU value parameters for the level-1 quota.
        self.parameter = parameter
        # Region ID.
        self.region_id = region_id
        # Resource status.
        self.status = status
        # The list of level-2 quotas.
        self.sub_quota_info_list = sub_quota_info_list
        # Tenant ID.
        self.tenant_id = tenant_id
        # Corresponds to the `resourceSystemType` field of the control cluster.
        self.type = type
        # Version number.
        self.version = version

    def validate(self):
        if self.parameter:
            self.parameter.validate()
        if self.sub_quota_info_list:
            for v1 in self.sub_quota_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.status is not None:
            result['status'] = self.status

        result['subQuotaInfoList'] = []
        if self.sub_quota_info_list is not None:
            for k1 in self.sub_quota_info_list:
                result['subQuotaInfoList'].append(k1.to_map() if k1 else None)

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.type is not None:
            result['type'] = self.type

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
            temp_model = main_models.GetComputeQuotaPlanResponseBodyDataQuotaParameter()
            self.parameter = temp_model.from_map(m.get('parameter'))

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('status') is not None:
            self.status = m.get('status')

        self.sub_quota_info_list = []
        if m.get('subQuotaInfoList') is not None:
            for k1 in m.get('subQuotaInfoList'):
                temp_model = main_models.GetComputeQuotaPlanResponseBodyDataQuotaSubQuotaInfoList()
                self.sub_quota_info_list.append(temp_model.from_map(k1))

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class GetComputeQuotaPlanResponseBodyDataQuotaSubQuotaInfoList(DaraModel):
    def __init__(
        self,
        cluster: str = None,
        create_time: int = None,
        creator_id: str = None,
        id: str = None,
        name: str = None,
        nick_name: str = None,
        parameter: main_models.GetComputeQuotaPlanResponseBodyDataQuotaSubQuotaInfoListParameter = None,
        region_id: str = None,
        status: str = None,
        tenant_id: str = None,
        type: str = None,
        version: str = None,
    ):
        # Cluster ID.
        self.cluster = cluster
        # Creation time.
        self.create_time = create_time
        # Creator cloud account UID.
        self.creator_id = creator_id
        # The ID of the level-2 quota.
        self.id = id
        # The name of the level-2 quota.
        self.name = name
        # The nickname of the level-2 quota.
        self.nick_name = nick_name
        # The parameters of the level-2 quota.
        self.parameter = parameter
        # Region ID.
        self.region_id = region_id
        # Resource status.
        self.status = status
        # Tenant ID.
        self.tenant_id = tenant_id
        # The type of quota.
        self.type = type
        # Version number.
        self.version = version

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.status is not None:
            result['status'] = self.status

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.type is not None:
            result['type'] = self.type

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
            temp_model = main_models.GetComputeQuotaPlanResponseBodyDataQuotaSubQuotaInfoListParameter()
            self.parameter = temp_model.from_map(m.get('parameter'))

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class GetComputeQuotaPlanResponseBodyDataQuotaSubQuotaInfoListParameter(DaraModel):
    def __init__(
        self,
        elastic_reserved_cu: int = None,
        enable_priority: bool = None,
        force_reserved_min: bool = None,
        max_cu: int = None,
        min_cu: int = None,
        scheduler_type: str = None,
        single_job_culimit: int = None,
    ):
        # The value of elastic Reserved CUs.
        self.elastic_reserved_cu = elastic_reserved_cu
        # whether to enable the priority feature.
        self.enable_priority = enable_priority
        # Whether it is exclusive.
        self.force_reserved_min = force_reserved_min
        # The value of maxCU in Reserved CUs.
        self.max_cu = max_cu
        # The value of minCU in Reserved CUs.
        self.min_cu = min_cu
        # Scheduling policy.
        self.scheduler_type = scheduler_type
        # The upper limit for CUs that can be concurrently used by a job scheduled to the quota.
        self.single_job_culimit = single_job_culimit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.elastic_reserved_cu is not None:
            result['elasticReservedCU'] = self.elastic_reserved_cu

        if self.enable_priority is not None:
            result['enablePriority'] = self.enable_priority

        if self.force_reserved_min is not None:
            result['forceReservedMin'] = self.force_reserved_min

        if self.max_cu is not None:
            result['maxCU'] = self.max_cu

        if self.min_cu is not None:
            result['minCU'] = self.min_cu

        if self.scheduler_type is not None:
            result['schedulerType'] = self.scheduler_type

        if self.single_job_culimit is not None:
            result['singleJobCULimit'] = self.single_job_culimit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('elasticReservedCU') is not None:
            self.elastic_reserved_cu = m.get('elasticReservedCU')

        if m.get('enablePriority') is not None:
            self.enable_priority = m.get('enablePriority')

        if m.get('forceReservedMin') is not None:
            self.force_reserved_min = m.get('forceReservedMin')

        if m.get('maxCU') is not None:
            self.max_cu = m.get('maxCU')

        if m.get('minCU') is not None:
            self.min_cu = m.get('minCU')

        if m.get('schedulerType') is not None:
            self.scheduler_type = m.get('schedulerType')

        if m.get('singleJobCULimit') is not None:
            self.single_job_culimit = m.get('singleJobCULimit')

        return self

class GetComputeQuotaPlanResponseBodyDataQuotaParameter(DaraModel):
    def __init__(
        self,
        elastic_reserved_cu: int = None,
        max_cu: int = None,
        min_cu: int = None,
    ):
        # The value of elastic Reserved CUs.
        self.elastic_reserved_cu = elastic_reserved_cu
        # The value of maxCU in Reserved CUs.
        self.max_cu = max_cu
        # The value of minCU in Reserved CUs.
        self.min_cu = min_cu

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.elastic_reserved_cu is not None:
            result['elasticReservedCU'] = self.elastic_reserved_cu

        if self.max_cu is not None:
            result['maxCU'] = self.max_cu

        if self.min_cu is not None:
            result['minCU'] = self.min_cu

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('elasticReservedCU') is not None:
            self.elastic_reserved_cu = m.get('elasticReservedCU')

        if m.get('maxCU') is not None:
            self.max_cu = m.get('maxCU')

        if m.get('minCU') is not None:
            self.min_cu = m.get('minCU')

        return self

