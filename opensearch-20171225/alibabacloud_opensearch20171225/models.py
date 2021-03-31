# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class CompileSortScriptResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CompileSortScriptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CompileSortScriptResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CompileSortScriptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateABTestExperimentResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        params: Dict[str, Any] = None,
        traffic: int = None,
        online: bool = None,
        name: str = None,
        updated: int = None,
        id: str = None,
    ):
        self.created = created
        self.params = params
        self.traffic = traffic
        self.online = online
        self.name = name
        self.updated = updated
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.params is not None:
            result['params'] = self.params
        if self.traffic is not None:
            result['traffic'] = self.traffic
        if self.online is not None:
            result['online'] = self.online
        if self.name is not None:
            result['name'] = self.name
        if self.updated is not None:
            result['updated'] = self.updated
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('params') is not None:
            self.params = m.get('params')
        if m.get('traffic') is not None:
            self.traffic = m.get('traffic')
        if m.get('online') is not None:
            self.online = m.get('online')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class CreateABTestExperimentResponseBody(TeaModel):
    def __init__(
        self,
        result: CreateABTestExperimentResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = CreateABTestExperimentResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateABTestExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateABTestExperimentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateABTestExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateABTestGroupResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        status: int = None,
        updated: int = None,
        name: str = None,
        id: str = None,
    ):
        self.created = created
        self.status = status
        self.updated = updated
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.status is not None:
            result['status'] = self.status
        if self.updated is not None:
            result['updated'] = self.updated
        if self.name is not None:
            result['name'] = self.name
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class CreateABTestGroupResponseBody(TeaModel):
    def __init__(
        self,
        result: CreateABTestGroupResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = CreateABTestGroupResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateABTestGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateABTestGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateABTestGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateABTestSceneResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        values: List[str] = None,
        status: int = None,
        updated: int = None,
        name: str = None,
        id: str = None,
    ):
        self.created = created
        self.values = values
        self.status = status
        self.updated = updated
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.values is not None:
            result['values'] = self.values
        if self.status is not None:
            result['status'] = self.status
        if self.updated is not None:
            result['updated'] = self.updated
        if self.name is not None:
            result['name'] = self.name
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('values') is not None:
            self.values = m.get('values')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class CreateABTestSceneResponseBody(TeaModel):
    def __init__(
        self,
        result: CreateABTestSceneResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = CreateABTestSceneResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateABTestSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateABTestSceneResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateABTestSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppRequest(TeaModel):
    def __init__(
        self,
        dry_run: bool = None,
    ):
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CreateAppResponseBody(TeaModel):
    def __init__(
        self,
        result: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAppResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppGroupResponseBodyResultQuota(TeaModel):
    def __init__(
        self,
        spec: str = None,
        doc_size: int = None,
        compute_resource: int = None,
    ):
        self.spec = spec
        self.doc_size = doc_size
        self.compute_resource = compute_resource

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spec is not None:
            result['spec'] = self.spec
        if self.doc_size is not None:
            result['docSize'] = self.doc_size
        if self.compute_resource is not None:
            result['computeResource'] = self.compute_resource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('docSize') is not None:
            self.doc_size = m.get('docSize')
        if m.get('computeResource') is not None:
            self.compute_resource = m.get('computeResource')
        return self


class CreateAppGroupResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        current_version: str = None,
        pending_second_rank_algo_deployment_id: int = None,
        lock_mode: str = None,
        updated: int = None,
        id: str = None,
        charge_type: str = None,
        has_pending_quota_review_task: int = None,
        second_rank_algo_deployment_id: int = None,
        quota: CreateAppGroupResponseBodyResultQuota = None,
        name: str = None,
        processing_order_id: str = None,
        instance_id: str = None,
        type: str = None,
        charging_way: int = None,
        status: str = None,
        project_id: str = None,
        commodity_code: str = None,
        switched_time: int = None,
        expire_on: str = None,
        domain: str = None,
        description: str = None,
        first_rank_algo_deployment_id: int = None,
        produced: int = None,
        locked_by_expiration: int = None,
    ):
        self.created = created
        self.current_version = current_version
        self.pending_second_rank_algo_deployment_id = pending_second_rank_algo_deployment_id
        self.lock_mode = lock_mode
        self.updated = updated
        self.id = id
        self.charge_type = charge_type
        self.has_pending_quota_review_task = has_pending_quota_review_task
        self.second_rank_algo_deployment_id = second_rank_algo_deployment_id
        self.quota = quota
        self.name = name
        self.processing_order_id = processing_order_id
        self.instance_id = instance_id
        self.type = type
        self.charging_way = charging_way
        self.status = status
        self.project_id = project_id
        self.commodity_code = commodity_code
        self.switched_time = switched_time
        self.expire_on = expire_on
        self.domain = domain
        self.description = description
        self.first_rank_algo_deployment_id = first_rank_algo_deployment_id
        self.produced = produced
        self.locked_by_expiration = locked_by_expiration

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.current_version is not None:
            result['currentVersion'] = self.current_version
        if self.pending_second_rank_algo_deployment_id is not None:
            result['pendingSecondRankAlgoDeploymentId'] = self.pending_second_rank_algo_deployment_id
        if self.lock_mode is not None:
            result['lockMode'] = self.lock_mode
        if self.updated is not None:
            result['updated'] = self.updated
        if self.id is not None:
            result['id'] = self.id
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.has_pending_quota_review_task is not None:
            result['hasPendingQuotaReviewTask'] = self.has_pending_quota_review_task
        if self.second_rank_algo_deployment_id is not None:
            result['secondRankAlgoDeploymentId'] = self.second_rank_algo_deployment_id
        if self.quota is not None:
            result['quota'] = self.quota.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.processing_order_id is not None:
            result['processingOrderId'] = self.processing_order_id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.type is not None:
            result['type'] = self.type
        if self.charging_way is not None:
            result['chargingWay'] = self.charging_way
        if self.status is not None:
            result['status'] = self.status
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.switched_time is not None:
            result['switchedTime'] = self.switched_time
        if self.expire_on is not None:
            result['expireOn'] = self.expire_on
        if self.domain is not None:
            result['domain'] = self.domain
        if self.description is not None:
            result['description'] = self.description
        if self.first_rank_algo_deployment_id is not None:
            result['firstRankAlgoDeploymentId'] = self.first_rank_algo_deployment_id
        if self.produced is not None:
            result['produced'] = self.produced
        if self.locked_by_expiration is not None:
            result['lockedByExpiration'] = self.locked_by_expiration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('currentVersion') is not None:
            self.current_version = m.get('currentVersion')
        if m.get('pendingSecondRankAlgoDeploymentId') is not None:
            self.pending_second_rank_algo_deployment_id = m.get('pendingSecondRankAlgoDeploymentId')
        if m.get('lockMode') is not None:
            self.lock_mode = m.get('lockMode')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('hasPendingQuotaReviewTask') is not None:
            self.has_pending_quota_review_task = m.get('hasPendingQuotaReviewTask')
        if m.get('secondRankAlgoDeploymentId') is not None:
            self.second_rank_algo_deployment_id = m.get('secondRankAlgoDeploymentId')
        if m.get('quota') is not None:
            temp_model = CreateAppGroupResponseBodyResultQuota()
            self.quota = temp_model.from_map(m['quota'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('processingOrderId') is not None:
            self.processing_order_id = m.get('processingOrderId')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('chargingWay') is not None:
            self.charging_way = m.get('chargingWay')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('switchedTime') is not None:
            self.switched_time = m.get('switchedTime')
        if m.get('expireOn') is not None:
            self.expire_on = m.get('expireOn')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('firstRankAlgoDeploymentId') is not None:
            self.first_rank_algo_deployment_id = m.get('firstRankAlgoDeploymentId')
        if m.get('produced') is not None:
            self.produced = m.get('produced')
        if m.get('lockedByExpiration') is not None:
            self.locked_by_expiration = m.get('lockedByExpiration')
        return self


class CreateAppGroupResponseBody(TeaModel):
    def __init__(
        self,
        result: CreateAppGroupResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = CreateAppGroupResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateAppGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAppGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAppGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDataCollectionResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        data_collection_type: str = None,
        type: str = None,
        industry_name: str = None,
        status: int = None,
        updated: int = None,
        name: str = None,
        sundial_id: str = None,
        id: str = None,
    ):
        self.created = created
        self.data_collection_type = data_collection_type
        self.type = type
        self.industry_name = industry_name
        self.status = status
        self.updated = updated
        self.name = name
        self.sundial_id = sundial_id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.data_collection_type is not None:
            result['dataCollectionType'] = self.data_collection_type
        if self.type is not None:
            result['type'] = self.type
        if self.industry_name is not None:
            result['industryName'] = self.industry_name
        if self.status is not None:
            result['status'] = self.status
        if self.updated is not None:
            result['updated'] = self.updated
        if self.name is not None:
            result['name'] = self.name
        if self.sundial_id is not None:
            result['sundialId'] = self.sundial_id
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('dataCollectionType') is not None:
            self.data_collection_type = m.get('dataCollectionType')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('industryName') is not None:
            self.industry_name = m.get('industryName')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sundialId') is not None:
            self.sundial_id = m.get('sundialId')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class CreateDataCollectionResponseBody(TeaModel):
    def __init__(
        self,
        result: CreateDataCollectionResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = CreateDataCollectionResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateDataCollectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDataCollectionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDataCollectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFirstRankRequest(TeaModel):
    def __init__(
        self,
        dry_run: bool = None,
    ):
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CreateFirstRankResponseBodyResultMeta(TeaModel):
    def __init__(
        self,
        arg: str = None,
        attribute: str = None,
        weight: float = None,
    ):
        self.arg = arg
        self.attribute = attribute
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arg is not None:
            result['arg'] = self.arg
        if self.attribute is not None:
            result['attribute'] = self.attribute
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arg') is not None:
            self.arg = m.get('arg')
        if m.get('attribute') is not None:
            self.attribute = m.get('attribute')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class CreateFirstRankResponseBodyResult(TeaModel):
    def __init__(
        self,
        active: bool = None,
        name: str = None,
        meta: List[CreateFirstRankResponseBodyResultMeta] = None,
    ):
        self.active = active
        self.name = name
        self.meta = meta

    def validate(self):
        if self.meta:
            for k in self.meta:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.name is not None:
            result['name'] = self.name
        result['meta'] = []
        if self.meta is not None:
            for k in self.meta:
                result['meta'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.meta = []
        if m.get('meta') is not None:
            for k in m.get('meta'):
                temp_model = CreateFirstRankResponseBodyResultMeta()
                self.meta.append(temp_model.from_map(k))
        return self


class CreateFirstRankResponseBody(TeaModel):
    def __init__(
        self,
        result: CreateFirstRankResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = CreateFirstRankResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateFirstRankResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateFirstRankResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateFirstRankResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInterventionDictionaryResponseBodyResult(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        analyzer: str = None,
        created: str = None,
        updated: str = None,
    ):
        self.name = name
        self.type = type
        self.analyzer = analyzer
        self.created = created
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.analyzer is not None:
            result['analyzer'] = self.analyzer
        if self.created is not None:
            result['created'] = self.created
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('analyzer') is not None:
            self.analyzer = m.get('analyzer')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class CreateInterventionDictionaryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CreateInterventionDictionaryResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = CreateInterventionDictionaryResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class CreateInterventionDictionaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateInterventionDictionaryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateInterventionDictionaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateModelResponseBody(TeaModel):
    def __init__(
        self,
        result: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateModelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateQueryProcessorRequest(TeaModel):
    def __init__(
        self,
        dry_run: bool = None,
    ):
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CreateQueryProcessorResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        active: bool = None,
        domain: str = None,
        indexes: List[str] = None,
        processors: List[Dict[str, Any]] = None,
        updated: int = None,
        name: str = None,
    ):
        self.created = created
        self.active = active
        self.domain = domain
        self.indexes = indexes
        self.processors = processors
        self.updated = updated
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.active is not None:
            result['active'] = self.active
        if self.domain is not None:
            result['domain'] = self.domain
        if self.indexes is not None:
            result['indexes'] = self.indexes
        if self.processors is not None:
            result['processors'] = self.processors
        if self.updated is not None:
            result['updated'] = self.updated
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('indexes') is not None:
            self.indexes = m.get('indexes')
        if m.get('processors') is not None:
            self.processors = m.get('processors')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CreateQueryProcessorResponseBody(TeaModel):
    def __init__(
        self,
        result: CreateQueryProcessorResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = CreateQueryProcessorResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateQueryProcessorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateQueryProcessorResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateQueryProcessorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateScheduledTaskResponseBody(TeaModel):
    def __init__(
        self,
        result: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateScheduledTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateScheduledTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateScheduledTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSecondRankRequest(TeaModel):
    def __init__(
        self,
        dry_run: bool = None,
    ):
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CreateSecondRankResponseBody(TeaModel):
    def __init__(
        self,
        result: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateSecondRankResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSecondRankResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateSecondRankResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSortScriptResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateSortScriptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSortScriptResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateSortScriptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserAnalyzerResponseBody(TeaModel):
    def __init__(
        self,
        result: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateUserAnalyzerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateUserAnalyzerResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateUserAnalyzerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteABTestExperimentResponseBody(TeaModel):
    def __init__(
        self,
        result: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteABTestExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteABTestExperimentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteABTestExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteABTestGroupResponseBody(TeaModel):
    def __init__(
        self,
        result: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteABTestGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteABTestGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteABTestGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteABTestSceneResponseBody(TeaModel):
    def __init__(
        self,
        result: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteABTestSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteABTestSceneResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteABTestSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteModelResponseBody(TeaModel):
    def __init__(
        self,
        result: str = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteModelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSortScriptResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteSortScriptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSortScriptResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteSortScriptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSortScriptFileResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteSortScriptFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSortScriptFileResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteSortScriptFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeABTestExperimentResponseBodyResultParams(TeaModel):
    def __init__(
        self,
        first_formula_name: str = None,
    ):
        self.first_formula_name = first_formula_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.first_formula_name is not None:
            result['first_formula_name'] = self.first_formula_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('first_formula_name') is not None:
            self.first_formula_name = m.get('first_formula_name')
        return self


class DescribeABTestExperimentResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        params: DescribeABTestExperimentResponseBodyResultParams = None,
        traffic: int = None,
        online: bool = None,
        name: str = None,
        updated: int = None,
        id: str = None,
    ):
        self.created = created
        self.params = params
        self.traffic = traffic
        self.online = online
        self.name = name
        self.updated = updated
        self.id = id

    def validate(self):
        if self.params:
            self.params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.params is not None:
            result['params'] = self.params.to_map()
        if self.traffic is not None:
            result['traffic'] = self.traffic
        if self.online is not None:
            result['online'] = self.online
        if self.name is not None:
            result['name'] = self.name
        if self.updated is not None:
            result['updated'] = self.updated
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('params') is not None:
            temp_model = DescribeABTestExperimentResponseBodyResultParams()
            self.params = temp_model.from_map(m['params'])
        if m.get('traffic') is not None:
            self.traffic = m.get('traffic')
        if m.get('online') is not None:
            self.online = m.get('online')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class DescribeABTestExperimentResponseBody(TeaModel):
    def __init__(
        self,
        result: DescribeABTestExperimentResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = DescribeABTestExperimentResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DescribeABTestExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeABTestExperimentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeABTestExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeABTestGroupResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        status: int = None,
        updated: int = None,
        name: str = None,
        id: str = None,
    ):
        self.created = created
        self.status = status
        self.updated = updated
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.status is not None:
            result['status'] = self.status
        if self.updated is not None:
            result['updated'] = self.updated
        if self.name is not None:
            result['name'] = self.name
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class DescribeABTestGroupResponseBody(TeaModel):
    def __init__(
        self,
        result: DescribeABTestGroupResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = DescribeABTestGroupResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DescribeABTestGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeABTestGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeABTestGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeABTestSceneResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        values: List[str] = None,
        status: int = None,
        updated: int = None,
        name: str = None,
        id: str = None,
    ):
        self.created = created
        self.values = values
        self.status = status
        self.updated = updated
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.values is not None:
            result['values'] = self.values
        if self.status is not None:
            result['status'] = self.status
        if self.updated is not None:
            result['updated'] = self.updated
        if self.name is not None:
            result['name'] = self.name
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('values') is not None:
            self.values = m.get('values')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class DescribeABTestSceneResponseBody(TeaModel):
    def __init__(
        self,
        result: DescribeABTestSceneResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = DescribeABTestSceneResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DescribeABTestSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeABTestSceneResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeABTestSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppResponseBodyResultDomainFunctions(TeaModel):
    def __init__(
        self,
        service: List[str] = None,
        qp: List[str] = None,
        algo: List[str] = None,
    ):
        self.service = service
        self.qp = qp
        self.algo = algo

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service is not None:
            result['service'] = self.service
        if self.qp is not None:
            result['qp'] = self.qp
        if self.algo is not None:
            result['algo'] = self.algo
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('service') is not None:
            self.service = m.get('service')
        if m.get('qp') is not None:
            self.qp = m.get('qp')
        if m.get('algo') is not None:
            self.algo = m.get('algo')
        return self


class DescribeAppResponseBodyResultDomain(TeaModel):
    def __init__(
        self,
        functions: DescribeAppResponseBodyResultDomainFunctions = None,
        category: str = None,
        name: str = None,
    ):
        self.functions = functions
        self.category = category
        self.name = name

    def validate(self):
        if self.functions:
            self.functions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.functions is not None:
            result['functions'] = self.functions.to_map()
        if self.category is not None:
            result['category'] = self.category
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('functions') is not None:
            temp_model = DescribeAppResponseBodyResultDomainFunctions()
            self.functions = temp_model.from_map(m['functions'])
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DescribeAppResponseBodyResultQuota(TeaModel):
    def __init__(
        self,
        spec: str = None,
        qps: int = None,
        doc_size: int = None,
        compute_resource: int = None,
    ):
        self.spec = spec
        self.qps = qps
        self.doc_size = doc_size
        self.compute_resource = compute_resource

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spec is not None:
            result['spec'] = self.spec
        if self.qps is not None:
            result['qps'] = self.qps
        if self.doc_size is not None:
            result['docSize'] = self.doc_size
        if self.compute_resource is not None:
            result['computeResource'] = self.compute_resource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('qps') is not None:
            self.qps = m.get('qps')
        if m.get('docSize') is not None:
            self.doc_size = m.get('docSize')
        if m.get('computeResource') is not None:
            self.compute_resource = m.get('computeResource')
        return self


class DescribeAppResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        cluster_name: str = None,
        auto_switch: bool = None,
        type: str = None,
        status: str = None,
        schema: Dict[str, Any] = None,
        progress_percent: int = None,
        id: str = None,
        algo_deployment_id: int = None,
        domain: DescribeAppResponseBodyResultDomain = None,
        description: str = None,
        fetch_fields: List[str] = None,
        quota: DescribeAppResponseBodyResultQuota = None,
    ):
        self.created = created
        self.cluster_name = cluster_name
        self.auto_switch = auto_switch
        self.type = type
        self.status = status
        self.schema = schema
        self.progress_percent = progress_percent
        self.id = id
        self.algo_deployment_id = algo_deployment_id
        self.domain = domain
        self.description = description
        self.fetch_fields = fetch_fields
        self.quota = quota

    def validate(self):
        if self.domain:
            self.domain.validate()
        if self.quota:
            self.quota.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name
        if self.auto_switch is not None:
            result['autoSwitch'] = self.auto_switch
        if self.type is not None:
            result['type'] = self.type
        if self.status is not None:
            result['status'] = self.status
        if self.schema is not None:
            result['schema'] = self.schema
        if self.progress_percent is not None:
            result['progressPercent'] = self.progress_percent
        if self.id is not None:
            result['id'] = self.id
        if self.algo_deployment_id is not None:
            result['algoDeploymentId'] = self.algo_deployment_id
        if self.domain is not None:
            result['domain'] = self.domain.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.fetch_fields is not None:
            result['fetchFields'] = self.fetch_fields
        if self.quota is not None:
            result['quota'] = self.quota.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('autoSwitch') is not None:
            self.auto_switch = m.get('autoSwitch')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('schema') is not None:
            self.schema = m.get('schema')
        if m.get('progressPercent') is not None:
            self.progress_percent = m.get('progressPercent')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('algoDeploymentId') is not None:
            self.algo_deployment_id = m.get('algoDeploymentId')
        if m.get('domain') is not None:
            temp_model = DescribeAppResponseBodyResultDomain()
            self.domain = temp_model.from_map(m['domain'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('fetchFields') is not None:
            self.fetch_fields = m.get('fetchFields')
        if m.get('quota') is not None:
            temp_model = DescribeAppResponseBodyResultQuota()
            self.quota = temp_model.from_map(m['quota'])
        return self


class DescribeAppResponseBody(TeaModel):
    def __init__(
        self,
        result: DescribeAppResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = DescribeAppResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DescribeAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAppResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppGroupResponseBodyResultQuota(TeaModel):
    def __init__(
        self,
        spec: str = None,
        doc_size: int = None,
        compute_resource: int = None,
    ):
        self.spec = spec
        self.doc_size = doc_size
        self.compute_resource = compute_resource

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spec is not None:
            result['spec'] = self.spec
        if self.doc_size is not None:
            result['docSize'] = self.doc_size
        if self.compute_resource is not None:
            result['computeResource'] = self.compute_resource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('docSize') is not None:
            self.doc_size = m.get('docSize')
        if m.get('computeResource') is not None:
            self.compute_resource = m.get('computeResource')
        return self


class DescribeAppGroupResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        current_version: str = None,
        pending_second_rank_algo_deployment_id: int = None,
        lock_mode: str = None,
        updated: int = None,
        id: str = None,
        charge_type: str = None,
        has_pending_quota_review_task: int = None,
        second_rank_algo_deployment_id: int = None,
        quota: DescribeAppGroupResponseBodyResultQuota = None,
        name: str = None,
        processing_order_id: str = None,
        instance_id: str = None,
        type: str = None,
        charging_way: int = None,
        status: str = None,
        project_id: str = None,
        commodity_code: str = None,
        switched_time: int = None,
        expire_on: str = None,
        domain: str = None,
        description: str = None,
        first_rank_algo_deployment_id: int = None,
        produced: int = None,
        locked_by_expiration: int = None,
    ):
        self.created = created
        self.current_version = current_version
        self.pending_second_rank_algo_deployment_id = pending_second_rank_algo_deployment_id
        self.lock_mode = lock_mode
        self.updated = updated
        self.id = id
        self.charge_type = charge_type
        self.has_pending_quota_review_task = has_pending_quota_review_task
        self.second_rank_algo_deployment_id = second_rank_algo_deployment_id
        self.quota = quota
        self.name = name
        self.processing_order_id = processing_order_id
        self.instance_id = instance_id
        self.type = type
        self.charging_way = charging_way
        self.status = status
        self.project_id = project_id
        self.commodity_code = commodity_code
        self.switched_time = switched_time
        self.expire_on = expire_on
        self.domain = domain
        self.description = description
        self.first_rank_algo_deployment_id = first_rank_algo_deployment_id
        self.produced = produced
        self.locked_by_expiration = locked_by_expiration

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.current_version is not None:
            result['currentVersion'] = self.current_version
        if self.pending_second_rank_algo_deployment_id is not None:
            result['pendingSecondRankAlgoDeploymentId'] = self.pending_second_rank_algo_deployment_id
        if self.lock_mode is not None:
            result['lockMode'] = self.lock_mode
        if self.updated is not None:
            result['updated'] = self.updated
        if self.id is not None:
            result['id'] = self.id
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.has_pending_quota_review_task is not None:
            result['hasPendingQuotaReviewTask'] = self.has_pending_quota_review_task
        if self.second_rank_algo_deployment_id is not None:
            result['secondRankAlgoDeploymentId'] = self.second_rank_algo_deployment_id
        if self.quota is not None:
            result['quota'] = self.quota.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.processing_order_id is not None:
            result['processingOrderId'] = self.processing_order_id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.type is not None:
            result['type'] = self.type
        if self.charging_way is not None:
            result['chargingWay'] = self.charging_way
        if self.status is not None:
            result['status'] = self.status
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.switched_time is not None:
            result['switchedTime'] = self.switched_time
        if self.expire_on is not None:
            result['expireOn'] = self.expire_on
        if self.domain is not None:
            result['domain'] = self.domain
        if self.description is not None:
            result['description'] = self.description
        if self.first_rank_algo_deployment_id is not None:
            result['firstRankAlgoDeploymentId'] = self.first_rank_algo_deployment_id
        if self.produced is not None:
            result['produced'] = self.produced
        if self.locked_by_expiration is not None:
            result['lockedByExpiration'] = self.locked_by_expiration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('currentVersion') is not None:
            self.current_version = m.get('currentVersion')
        if m.get('pendingSecondRankAlgoDeploymentId') is not None:
            self.pending_second_rank_algo_deployment_id = m.get('pendingSecondRankAlgoDeploymentId')
        if m.get('lockMode') is not None:
            self.lock_mode = m.get('lockMode')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('hasPendingQuotaReviewTask') is not None:
            self.has_pending_quota_review_task = m.get('hasPendingQuotaReviewTask')
        if m.get('secondRankAlgoDeploymentId') is not None:
            self.second_rank_algo_deployment_id = m.get('secondRankAlgoDeploymentId')
        if m.get('quota') is not None:
            temp_model = DescribeAppGroupResponseBodyResultQuota()
            self.quota = temp_model.from_map(m['quota'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('processingOrderId') is not None:
            self.processing_order_id = m.get('processingOrderId')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('chargingWay') is not None:
            self.charging_way = m.get('chargingWay')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('switchedTime') is not None:
            self.switched_time = m.get('switchedTime')
        if m.get('expireOn') is not None:
            self.expire_on = m.get('expireOn')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('firstRankAlgoDeploymentId') is not None:
            self.first_rank_algo_deployment_id = m.get('firstRankAlgoDeploymentId')
        if m.get('produced') is not None:
            self.produced = m.get('produced')
        if m.get('lockedByExpiration') is not None:
            self.locked_by_expiration = m.get('lockedByExpiration')
        return self


class DescribeAppGroupResponseBody(TeaModel):
    def __init__(
        self,
        result: DescribeAppGroupResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = DescribeAppGroupResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DescribeAppGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAppGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAppGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppGroupDataReportRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
    ):
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        return self


class DescribeAppGroupDataReportResponseBodyResultReceivedSampleMessage(TeaModel):
    def __init__(
        self,
        event_id: int = None,
        arg_3: str = None,
        arg_1: str = None,
        sdk_version: str = None,
        user_id: str = None,
        page: str = None,
        args: str = None,
        session_id: str = None,
        sdk_type: str = None,
        client_ip: str = None,
    ):
        self.event_id = event_id
        self.arg_3 = arg_3
        self.arg_1 = arg_1
        self.sdk_version = sdk_version
        self.user_id = user_id
        self.page = page
        self.args = args
        self.session_id = session_id
        self.sdk_type = sdk_type
        self.client_ip = client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['eventId'] = self.event_id
        if self.arg_3 is not None:
            result['arg3'] = self.arg_3
        if self.arg_1 is not None:
            result['arg1'] = self.arg_1
        if self.sdk_version is not None:
            result['sdkVersion'] = self.sdk_version
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.page is not None:
            result['page'] = self.page
        if self.args is not None:
            result['args'] = self.args
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.sdk_type is not None:
            result['sdkType'] = self.sdk_type
        if self.client_ip is not None:
            result['clientIp'] = self.client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('eventId') is not None:
            self.event_id = m.get('eventId')
        if m.get('arg3') is not None:
            self.arg_3 = m.get('arg3')
        if m.get('arg1') is not None:
            self.arg_1 = m.get('arg1')
        if m.get('sdkVersion') is not None:
            self.sdk_version = m.get('sdkVersion')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('args') is not None:
            self.args = m.get('args')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('sdkType') is not None:
            self.sdk_type = m.get('sdkType')
        if m.get('clientIp') is not None:
            self.client_ip = m.get('clientIp')
        return self


class DescribeAppGroupDataReportResponseBodyResultReceivedSample(TeaModel):
    def __init__(
        self,
        received_time_ms: int = None,
        message: DescribeAppGroupDataReportResponseBodyResultReceivedSampleMessage = None,
    ):
        self.received_time_ms = received_time_ms
        self.message = message

    def validate(self):
        if self.message:
            self.message.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.received_time_ms is not None:
            result['receivedTimeMs'] = self.received_time_ms
        if self.message is not None:
            result['message'] = self.message.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('receivedTimeMs') is not None:
            self.received_time_ms = m.get('receivedTimeMs')
        if m.get('message') is not None:
            temp_model = DescribeAppGroupDataReportResponseBodyResultReceivedSampleMessage()
            self.message = temp_model.from_map(m['message'])
        return self


class DescribeAppGroupDataReportResponseBodyResult(TeaModel):
    def __init__(
        self,
        received_sample: List[DescribeAppGroupDataReportResponseBodyResultReceivedSample] = None,
        received_count: int = None,
    ):
        self.received_sample = received_sample
        self.received_count = received_count

    def validate(self):
        if self.received_sample:
            for k in self.received_sample:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['receivedSample'] = []
        if self.received_sample is not None:
            for k in self.received_sample:
                result['receivedSample'].append(k.to_map() if k else None)
        if self.received_count is not None:
            result['receivedCount'] = self.received_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.received_sample = []
        if m.get('receivedSample') is not None:
            for k in m.get('receivedSample'):
                temp_model = DescribeAppGroupDataReportResponseBodyResultReceivedSample()
                self.received_sample.append(temp_model.from_map(k))
        if m.get('receivedCount') is not None:
            self.received_count = m.get('receivedCount')
        return self


class DescribeAppGroupDataReportResponseBody(TeaModel):
    def __init__(
        self,
        result: DescribeAppGroupDataReportResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = DescribeAppGroupDataReportResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DescribeAppGroupDataReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAppGroupDataReportResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAppGroupDataReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppsResponseBody(TeaModel):
    def __init__(
        self,
        result: List[Dict[str, Any]] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DescribeAppsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAppsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        result: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DescribeAppStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAppStatisticsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAppStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataCollctionResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        data_collection_type: str = None,
        type: str = None,
        industry_name: str = None,
        status: int = None,
        updated: int = None,
        name: str = None,
        sundial_id: str = None,
        id: str = None,
    ):
        self.created = created
        self.data_collection_type = data_collection_type
        self.type = type
        self.industry_name = industry_name
        self.status = status
        self.updated = updated
        self.name = name
        self.sundial_id = sundial_id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.data_collection_type is not None:
            result['dataCollectionType'] = self.data_collection_type
        if self.type is not None:
            result['type'] = self.type
        if self.industry_name is not None:
            result['industryName'] = self.industry_name
        if self.status is not None:
            result['status'] = self.status
        if self.updated is not None:
            result['updated'] = self.updated
        if self.name is not None:
            result['name'] = self.name
        if self.sundial_id is not None:
            result['sundialId'] = self.sundial_id
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('dataCollectionType') is not None:
            self.data_collection_type = m.get('dataCollectionType')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('industryName') is not None:
            self.industry_name = m.get('industryName')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sundialId') is not None:
            self.sundial_id = m.get('sundialId')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class DescribeDataCollctionResponseBody(TeaModel):
    def __init__(
        self,
        result: DescribeDataCollctionResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = DescribeDataCollctionResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DescribeDataCollctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDataCollctionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDataCollctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFirstRankResponseBodyResultMeta(TeaModel):
    def __init__(
        self,
        arg: str = None,
        attribute: str = None,
        weight: float = None,
    ):
        self.arg = arg
        self.attribute = attribute
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arg is not None:
            result['arg'] = self.arg
        if self.attribute is not None:
            result['attribute'] = self.attribute
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arg') is not None:
            self.arg = m.get('arg')
        if m.get('attribute') is not None:
            self.attribute = m.get('attribute')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class DescribeFirstRankResponseBodyResult(TeaModel):
    def __init__(
        self,
        active: bool = None,
        description: str = None,
        name: str = None,
        meta: List[DescribeFirstRankResponseBodyResultMeta] = None,
    ):
        self.active = active
        self.description = description
        self.name = name
        self.meta = meta

    def validate(self):
        if self.meta:
            for k in self.meta:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        result['meta'] = []
        if self.meta is not None:
            for k in self.meta:
                result['meta'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.meta = []
        if m.get('meta') is not None:
            for k in m.get('meta'):
                temp_model = DescribeFirstRankResponseBodyResultMeta()
                self.meta.append(temp_model.from_map(k))
        return self


class DescribeFirstRankResponseBody(TeaModel):
    def __init__(
        self,
        result: DescribeFirstRankResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = DescribeFirstRankResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DescribeFirstRankResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFirstRankResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFirstRankResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInterventionDictionaryResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: str = None,
        type: str = None,
        analyzer: str = None,
        updated: str = None,
        name: str = None,
    ):
        self.created = created
        self.type = type
        self.analyzer = analyzer
        self.updated = updated
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.type is not None:
            result['type'] = self.type
        if self.analyzer is not None:
            result['analyzer'] = self.analyzer
        if self.updated is not None:
            result['updated'] = self.updated
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('analyzer') is not None:
            self.analyzer = m.get('analyzer')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DescribeInterventionDictionaryResponseBody(TeaModel):
    def __init__(
        self,
        result: DescribeInterventionDictionaryResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = DescribeInterventionDictionaryResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DescribeInterventionDictionaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInterventionDictionaryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInterventionDictionaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeModelResponseBody(TeaModel):
    def __init__(
        self,
        result: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DescribeModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeModelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeQueryProcessorResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        active: bool = None,
        domain: str = None,
        indexes: List[str] = None,
        processors: List[Dict[str, Any]] = None,
        updated: int = None,
        name: str = None,
    ):
        self.created = created
        self.active = active
        self.domain = domain
        self.indexes = indexes
        self.processors = processors
        self.updated = updated
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.active is not None:
            result['active'] = self.active
        if self.domain is not None:
            result['domain'] = self.domain
        if self.indexes is not None:
            result['indexes'] = self.indexes
        if self.processors is not None:
            result['processors'] = self.processors
        if self.updated is not None:
            result['updated'] = self.updated
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('indexes') is not None:
            self.indexes = m.get('indexes')
        if m.get('processors') is not None:
            self.processors = m.get('processors')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DescribeQueryProcessorResponseBody(TeaModel):
    def __init__(
        self,
        result: DescribeQueryProcessorResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = DescribeQueryProcessorResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DescribeQueryProcessorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeQueryProcessorResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeQueryProcessorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionResponseBodyResult(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        config: Dict[str, Any] = None,
    ):
        self.region_id = region_id
        self.config = config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.config is not None:
            result['config'] = self.config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('config') is not None:
            self.config = m.get('config')
        return self


class DescribeRegionResponseBody(TeaModel):
    def __init__(
        self,
        result: DescribeRegionResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = DescribeRegionResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DescribeRegionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRegionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRegionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsResponseBodyResult(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        endpoint: str = None,
        local_name: str = None,
        console_url: str = None,
    ):
        self.region_id = region_id
        self.endpoint = endpoint
        self.local_name = local_name
        self.console_url = console_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.local_name is not None:
            result['localName'] = self.local_name
        if self.console_url is not None:
            result['consoleUrl'] = self.console_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('localName') is not None:
            self.local_name = m.get('localName')
        if m.get('consoleUrl') is not None:
            self.console_url = m.get('consoleUrl')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        result: List[DescribeRegionsResponseBodyResult] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = DescribeRegionsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScheduledTaskResponseBody(TeaModel):
    def __init__(
        self,
        result: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DescribeScheduledTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScheduledTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeScheduledTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSecondRankResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        active: bool = None,
        is_default: str = None,
        is_sys: str = None,
        description: str = None,
        updated: int = None,
        name: str = None,
        meta: str = None,
        id: str = None,
    ):
        self.created = created
        self.active = active
        self.is_default = is_default
        self.is_sys = is_sys
        self.description = description
        self.updated = updated
        self.name = name
        self.meta = meta
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.active is not None:
            result['active'] = self.active
        if self.is_default is not None:
            result['isDefault'] = self.is_default
        if self.is_sys is not None:
            result['isSys'] = self.is_sys
        if self.description is not None:
            result['description'] = self.description
        if self.updated is not None:
            result['updated'] = self.updated
        if self.name is not None:
            result['name'] = self.name
        if self.meta is not None:
            result['meta'] = self.meta
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('isDefault') is not None:
            self.is_default = m.get('isDefault')
        if m.get('isSys') is not None:
            self.is_sys = m.get('isSys')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class DescribeSecondRankResponseBody(TeaModel):
    def __init__(
        self,
        result: DescribeSecondRankResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = DescribeSecondRankResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DescribeSecondRankResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSecondRankResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSecondRankResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSlowQueryStatusResponseBodyResult(TeaModel):
    def __init__(
        self,
        region: str = None,
        status: str = None,
        app_group_id: str = None,
    ):
        self.region = region
        self.status = status
        self.app_group_id = app_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['region'] = self.region
        if self.status is not None:
            result['status'] = self.status
        if self.app_group_id is not None:
            result['appGroupId'] = self.app_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('appGroupId') is not None:
            self.app_group_id = m.get('appGroupId')
        return self


class DescribeSlowQueryStatusResponseBody(TeaModel):
    def __init__(
        self,
        result: DescribeSlowQueryStatusResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = DescribeSlowQueryStatusResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DescribeSlowQueryStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSlowQueryStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSlowQueryStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserAnalyzerRequest(TeaModel):
    def __init__(
        self,
        with_: str = None,
    ):
        self.with_ = with_

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.with_ is not None:
            result['with'] = self.with_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('with') is not None:
            self.with_ = m.get('with')
        return self


class DescribeUserAnalyzerResponseBody(TeaModel):
    def __init__(
        self,
        result: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DescribeUserAnalyzerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUserAnalyzerResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeUserAnalyzerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableSlowQueryResponseBody(TeaModel):
    def __init__(
        self,
        result: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DisableSlowQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableSlowQueryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DisableSlowQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableSlowQueryResponseBody(TeaModel):
    def __init__(
        self,
        result: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class EnableSlowQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableSlowQueryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EnableSlowQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDomainRequest(TeaModel):
    def __init__(
        self,
        app_group_identity: str = None,
    ):
        self.app_group_identity = app_group_identity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_group_identity is not None:
            result['appGroupIdentity'] = self.app_group_identity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appGroupIdentity') is not None:
            self.app_group_identity = m.get('appGroupIdentity')
        return self


class GetDomainResponseBody(TeaModel):
    def __init__(
        self,
        result: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDomainResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetModelProgressResponseBodyResult(TeaModel):
    def __init__(
        self,
        status: str = None,
        progress: int = None,
    ):
        self.status = status
        self.progress = progress

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['status'] = self.status
        if self.progress is not None:
            result['progress'] = self.progress
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('progress') is not None:
            self.progress = m.get('progress')
        return self


class GetModelProgressResponseBody(TeaModel):
    def __init__(
        self,
        result: GetModelProgressResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = GetModelProgressResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetModelProgressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetModelProgressResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetModelProgressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetModelReportResponseBody(TeaModel):
    def __init__(
        self,
        result: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetModelReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetModelReportResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetModelReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetScriptFileNamesResponseBodyResult(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        create_time: str = None,
        modify_time: str = None,
    ):
        self.file_name = file_name
        self.create_time = create_time
        self.modify_time = modify_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.modify_time is not None:
            result['modifyTime'] = self.modify_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')
        return self


class GetScriptFileNamesResponseBody(TeaModel):
    def __init__(
        self,
        result: List[GetScriptFileNamesResponseBodyResult] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = GetScriptFileNamesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetScriptFileNamesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetScriptFileNamesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetScriptFileNamesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSortScriptResponseBodyResult(TeaModel):
    def __init__(
        self,
        type: str = None,
        scope: str = None,
        create_time: str = None,
        status: str = None,
        modify_time: str = None,
    ):
        self.type = type
        self.scope = scope
        self.create_time = create_time
        self.status = status
        self.modify_time = modify_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.scope is not None:
            result['scope'] = self.scope
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.status is not None:
            result['status'] = self.status
        if self.modify_time is not None:
            result['modifyTime'] = self.modify_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')
        return self


class GetSortScriptResponseBody(TeaModel):
    def __init__(
        self,
        result: GetSortScriptResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = GetSortScriptResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetSortScriptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSortScriptResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetSortScriptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSortScriptFileResponseBodyResult(TeaModel):
    def __init__(
        self,
        content: str = None,
        create_time: str = None,
        modify_time: str = None,
        version: int = None,
    ):
        self.content = content
        self.create_time = create_time
        self.modify_time = modify_time
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.modify_time is not None:
            result['modifyTime'] = self.modify_time
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetSortScriptFileResponseBody(TeaModel):
    def __init__(
        self,
        result: GetSortScriptFileResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = GetSortScriptFileResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetSortScriptFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSortScriptFileResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetSortScriptFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetValidationErrorRequest(TeaModel):
    def __init__(
        self,
        error_code: str = None,
    ):
        self.error_code = error_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        return self


class GetValidationErrorResponseBody(TeaModel):
    def __init__(
        self,
        result: List[Dict[str, Any]] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetValidationErrorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetValidationErrorResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetValidationErrorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetValidationReportRequest(TeaModel):
    def __init__(
        self,
        type: str = None,
    ):
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetValidationReportResponseBody(TeaModel):
    def __init__(
        self,
        result: List[Dict[str, Any]] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetValidationReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetValidationReportResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetValidationReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListABTestExperimentsResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        params: Dict[str, Any] = None,
        traffic: int = None,
        online: bool = None,
        name: str = None,
        updated: int = None,
        id: str = None,
    ):
        self.created = created
        self.params = params
        self.traffic = traffic
        self.online = online
        self.name = name
        self.updated = updated
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.params is not None:
            result['params'] = self.params
        if self.traffic is not None:
            result['traffic'] = self.traffic
        if self.online is not None:
            result['online'] = self.online
        if self.name is not None:
            result['name'] = self.name
        if self.updated is not None:
            result['updated'] = self.updated
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('params') is not None:
            self.params = m.get('params')
        if m.get('traffic') is not None:
            self.traffic = m.get('traffic')
        if m.get('online') is not None:
            self.online = m.get('online')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class ListABTestExperimentsResponseBody(TeaModel):
    def __init__(
        self,
        result: List[ListABTestExperimentsResponseBodyResult] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListABTestExperimentsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListABTestExperimentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListABTestExperimentsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListABTestExperimentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListABTestFixedFlowDividersResponseBody(TeaModel):
    def __init__(
        self,
        result: List[str] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListABTestFixedFlowDividersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListABTestFixedFlowDividersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListABTestFixedFlowDividersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListABTestGroupsResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        status: int = None,
        updated: int = None,
        name: str = None,
        id: str = None,
    ):
        self.created = created
        self.status = status
        self.updated = updated
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.status is not None:
            result['status'] = self.status
        if self.updated is not None:
            result['updated'] = self.updated
        if self.name is not None:
            result['name'] = self.name
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class ListABTestGroupsResponseBody(TeaModel):
    def __init__(
        self,
        result: List[ListABTestGroupsResponseBodyResult] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListABTestGroupsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListABTestGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListABTestGroupsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListABTestGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListABTestMetricsResponseBodyResult(TeaModel):
    def __init__(
        self,
        zero_hit_rate: float = None,
        ctr: float = None,
        experiment_name: str = None,
        date: str = None,
        ipv_uv: int = None,
        ipv: int = None,
        uv: int = None,
        pv: int = None,
    ):
        self.zero_hit_rate = zero_hit_rate
        self.ctr = ctr
        self.experiment_name = experiment_name
        self.date = date
        self.ipv_uv = ipv_uv
        self.ipv = ipv
        self.uv = uv
        self.pv = pv

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.zero_hit_rate is not None:
            result['zeroHitRate'] = self.zero_hit_rate
        if self.ctr is not None:
            result['ctr'] = self.ctr
        if self.experiment_name is not None:
            result['experimentName'] = self.experiment_name
        if self.date is not None:
            result['date'] = self.date
        if self.ipv_uv is not None:
            result['ipvUv'] = self.ipv_uv
        if self.ipv is not None:
            result['ipv'] = self.ipv
        if self.uv is not None:
            result['uv'] = self.uv
        if self.pv is not None:
            result['pv'] = self.pv
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('zeroHitRate') is not None:
            self.zero_hit_rate = m.get('zeroHitRate')
        if m.get('ctr') is not None:
            self.ctr = m.get('ctr')
        if m.get('experimentName') is not None:
            self.experiment_name = m.get('experimentName')
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('ipvUv') is not None:
            self.ipv_uv = m.get('ipvUv')
        if m.get('ipv') is not None:
            self.ipv = m.get('ipv')
        if m.get('uv') is not None:
            self.uv = m.get('uv')
        if m.get('pv') is not None:
            self.pv = m.get('pv')
        return self


class ListABTestMetricsResponseBody(TeaModel):
    def __init__(
        self,
        result: List[ListABTestMetricsResponseBodyResult] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListABTestMetricsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListABTestMetricsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListABTestMetricsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListABTestMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListABTestScenesResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        values: List[str] = None,
        status: int = None,
        updated: int = None,
        name: str = None,
        id: str = None,
    ):
        self.created = created
        self.values = values
        self.status = status
        self.updated = updated
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.values is not None:
            result['values'] = self.values
        if self.status is not None:
            result['status'] = self.status
        if self.updated is not None:
            result['updated'] = self.updated
        if self.name is not None:
            result['name'] = self.name
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('values') is not None:
            self.values = m.get('values')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class ListABTestScenesResponseBody(TeaModel):
    def __init__(
        self,
        result: List[ListABTestScenesResponseBodyResult] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListABTestScenesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListABTestScenesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListABTestScenesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListABTestScenesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppGroupErrorsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        start_time: int = None,
        stop_time: int = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.app_id = app_id
        self.start_time = start_time
        self.stop_time = stop_time
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.stop_time is not None:
            result['stopTime'] = self.stop_time
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('stopTime') is not None:
            self.stop_time = m.get('stopTime')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListAppGroupErrorsResponseBody(TeaModel):
    def __init__(
        self,
        result: List[Dict[str, Any]] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.result = result
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListAppGroupErrorsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAppGroupErrorsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAppGroupErrorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppGroupMetricsRequest(TeaModel):
    def __init__(
        self,
        metric_type: str = None,
        start_time: int = None,
        end_time: int = None,
        indexes: str = None,
    ):
        self.metric_type = metric_type
        self.start_time = start_time
        self.end_time = end_time
        self.indexes = indexes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric_type is not None:
            result['metricType'] = self.metric_type
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.indexes is not None:
            result['indexes'] = self.indexes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metricType') is not None:
            self.metric_type = m.get('metricType')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('indexes') is not None:
            self.indexes = m.get('indexes')
        return self


class ListAppGroupMetricsResponseBody(TeaModel):
    def __init__(
        self,
        result: List[Dict[str, Any]] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListAppGroupMetricsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAppGroupMetricsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAppGroupMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppGroupsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        instance_id: str = None,
        name: str = None,
        type: str = None,
        sort_by: int = None,
        resource_group_id: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.instance_id = instance_id
        self.name = name
        self.type = type
        self.sort_by = sort_by
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.sort_by is not None:
            result['sortBy'] = self.sort_by
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('sortBy') is not None:
            self.sort_by = m.get('sortBy')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        return self


class ListAppGroupsResponseBodyResultQuota(TeaModel):
    def __init__(
        self,
        spec: str = None,
        doc_size: int = None,
        compute_resource: int = None,
    ):
        self.spec = spec
        self.doc_size = doc_size
        self.compute_resource = compute_resource

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spec is not None:
            result['spec'] = self.spec
        if self.doc_size is not None:
            result['docSize'] = self.doc_size
        if self.compute_resource is not None:
            result['computeResource'] = self.compute_resource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('docSize') is not None:
            self.doc_size = m.get('docSize')
        if m.get('computeResource') is not None:
            self.compute_resource = m.get('computeResource')
        return self


class ListAppGroupsResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        current_version: str = None,
        pending_second_rank_algo_deployment_id: int = None,
        lock_mode: str = None,
        updated: int = None,
        id: str = None,
        charge_type: str = None,
        has_pending_quota_review_task: int = None,
        second_rank_algo_deployment_id: int = None,
        quota: ListAppGroupsResponseBodyResultQuota = None,
        name: str = None,
        processing_order_id: str = None,
        instance_id: str = None,
        type: str = None,
        charging_way: int = None,
        status: str = None,
        project_id: str = None,
        commodity_code: str = None,
        switched_time: int = None,
        expire_on: str = None,
        domain: str = None,
        description: str = None,
        first_rank_algo_deployment_id: int = None,
        produced: int = None,
        locked_by_expiration: int = None,
    ):
        self.created = created
        self.current_version = current_version
        self.pending_second_rank_algo_deployment_id = pending_second_rank_algo_deployment_id
        self.lock_mode = lock_mode
        self.updated = updated
        self.id = id
        self.charge_type = charge_type
        self.has_pending_quota_review_task = has_pending_quota_review_task
        self.second_rank_algo_deployment_id = second_rank_algo_deployment_id
        self.quota = quota
        self.name = name
        self.processing_order_id = processing_order_id
        self.instance_id = instance_id
        self.type = type
        self.charging_way = charging_way
        self.status = status
        self.project_id = project_id
        self.commodity_code = commodity_code
        self.switched_time = switched_time
        self.expire_on = expire_on
        self.domain = domain
        self.description = description
        self.first_rank_algo_deployment_id = first_rank_algo_deployment_id
        self.produced = produced
        self.locked_by_expiration = locked_by_expiration

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.current_version is not None:
            result['currentVersion'] = self.current_version
        if self.pending_second_rank_algo_deployment_id is not None:
            result['pendingSecondRankAlgoDeploymentId'] = self.pending_second_rank_algo_deployment_id
        if self.lock_mode is not None:
            result['lockMode'] = self.lock_mode
        if self.updated is not None:
            result['updated'] = self.updated
        if self.id is not None:
            result['id'] = self.id
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.has_pending_quota_review_task is not None:
            result['hasPendingQuotaReviewTask'] = self.has_pending_quota_review_task
        if self.second_rank_algo_deployment_id is not None:
            result['secondRankAlgoDeploymentId'] = self.second_rank_algo_deployment_id
        if self.quota is not None:
            result['quota'] = self.quota.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.processing_order_id is not None:
            result['processingOrderId'] = self.processing_order_id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.type is not None:
            result['type'] = self.type
        if self.charging_way is not None:
            result['chargingWay'] = self.charging_way
        if self.status is not None:
            result['status'] = self.status
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.switched_time is not None:
            result['switchedTime'] = self.switched_time
        if self.expire_on is not None:
            result['expireOn'] = self.expire_on
        if self.domain is not None:
            result['domain'] = self.domain
        if self.description is not None:
            result['description'] = self.description
        if self.first_rank_algo_deployment_id is not None:
            result['firstRankAlgoDeploymentId'] = self.first_rank_algo_deployment_id
        if self.produced is not None:
            result['produced'] = self.produced
        if self.locked_by_expiration is not None:
            result['lockedByExpiration'] = self.locked_by_expiration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('currentVersion') is not None:
            self.current_version = m.get('currentVersion')
        if m.get('pendingSecondRankAlgoDeploymentId') is not None:
            self.pending_second_rank_algo_deployment_id = m.get('pendingSecondRankAlgoDeploymentId')
        if m.get('lockMode') is not None:
            self.lock_mode = m.get('lockMode')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('hasPendingQuotaReviewTask') is not None:
            self.has_pending_quota_review_task = m.get('hasPendingQuotaReviewTask')
        if m.get('secondRankAlgoDeploymentId') is not None:
            self.second_rank_algo_deployment_id = m.get('secondRankAlgoDeploymentId')
        if m.get('quota') is not None:
            temp_model = ListAppGroupsResponseBodyResultQuota()
            self.quota = temp_model.from_map(m['quota'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('processingOrderId') is not None:
            self.processing_order_id = m.get('processingOrderId')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('chargingWay') is not None:
            self.charging_way = m.get('chargingWay')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('switchedTime') is not None:
            self.switched_time = m.get('switchedTime')
        if m.get('expireOn') is not None:
            self.expire_on = m.get('expireOn')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('firstRankAlgoDeploymentId') is not None:
            self.first_rank_algo_deployment_id = m.get('firstRankAlgoDeploymentId')
        if m.get('produced') is not None:
            self.produced = m.get('produced')
        if m.get('lockedByExpiration') is not None:
            self.locked_by_expiration = m.get('lockedByExpiration')
        return self


class ListAppGroupsResponseBody(TeaModel):
    def __init__(
        self,
        result: List[ListAppGroupsResponseBodyResult] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.result = result
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListAppGroupsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListAppGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAppGroupsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAppGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppsRequest(TeaModel):
    def __init__(
        self,
        group: bool = None,
        page: int = None,
        size: int = None,
    ):
        self.group = group
        self.page = page
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group is not None:
            result['group'] = self.group
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('group') is not None:
            self.group = m.get('group')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListAppsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class ListDataCollectionsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListDataCollectionsResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        data_collection_type: str = None,
        type: str = None,
        industry_name: str = None,
        status: int = None,
        updated: int = None,
        name: str = None,
        sundial_id: str = None,
        id: str = None,
    ):
        self.created = created
        self.data_collection_type = data_collection_type
        self.type = type
        self.industry_name = industry_name
        self.status = status
        self.updated = updated
        self.name = name
        self.sundial_id = sundial_id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.data_collection_type is not None:
            result['dataCollectionType'] = self.data_collection_type
        if self.type is not None:
            result['type'] = self.type
        if self.industry_name is not None:
            result['industryName'] = self.industry_name
        if self.status is not None:
            result['status'] = self.status
        if self.updated is not None:
            result['updated'] = self.updated
        if self.name is not None:
            result['name'] = self.name
        if self.sundial_id is not None:
            result['sundialId'] = self.sundial_id
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('dataCollectionType') is not None:
            self.data_collection_type = m.get('dataCollectionType')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('industryName') is not None:
            self.industry_name = m.get('industryName')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sundialId') is not None:
            self.sundial_id = m.get('sundialId')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class ListDataCollectionsResponseBody(TeaModel):
    def __init__(
        self,
        result: List[ListDataCollectionsResponseBodyResult] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.result = result
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListDataCollectionsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListDataCollectionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDataCollectionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDataCollectionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeployedAlgorithmModelsRequest(TeaModel):
    def __init__(
        self,
        in_service_only: bool = None,
        algorithm_type: str = None,
    ):
        self.in_service_only = in_service_only
        self.algorithm_type = algorithm_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.in_service_only is not None:
            result['inServiceOnly'] = self.in_service_only
        if self.algorithm_type is not None:
            result['algorithmType'] = self.algorithm_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inServiceOnly') is not None:
            self.in_service_only = m.get('inServiceOnly')
        if m.get('algorithmType') is not None:
            self.algorithm_type = m.get('algorithmType')
        return self


class ListDeployedAlgorithmModelsResponseBodyResultModels(TeaModel):
    def __init__(
        self,
        model_name: str = None,
        project_id: int = None,
        model_id: int = None,
        algorithm_type: str = None,
        status: str = None,
        progress: int = None,
    ):
        self.model_name = model_name
        self.project_id = project_id
        self.model_id = model_id
        self.algorithm_type = algorithm_type
        self.status = status
        self.progress = progress

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_name is not None:
            result['modelName'] = self.model_name
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.algorithm_type is not None:
            result['algorithmType'] = self.algorithm_type
        if self.status is not None:
            result['status'] = self.status
        if self.progress is not None:
            result['progress'] = self.progress
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('algorithmType') is not None:
            self.algorithm_type = m.get('algorithmType')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('progress') is not None:
            self.progress = m.get('progress')
        return self


class ListDeployedAlgorithmModelsResponseBodyResult(TeaModel):
    def __init__(
        self,
        apps: List[str] = None,
        app_group_name: str = None,
        models: List[ListDeployedAlgorithmModelsResponseBodyResultModels] = None,
        gmt_modified: str = None,
        status: str = None,
        scene: str = None,
        gmt_create: str = None,
        id: str = None,
        desc: str = None,
    ):
        self.apps = apps
        self.app_group_name = app_group_name
        self.models = models
        self.gmt_modified = gmt_modified
        self.status = status
        self.scene = scene
        self.gmt_create = gmt_create
        self.id = id
        self.desc = desc

    def validate(self):
        if self.models:
            for k in self.models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apps is not None:
            result['apps'] = self.apps
        if self.app_group_name is not None:
            result['appGroupName'] = self.app_group_name
        result['models'] = []
        if self.models is not None:
            for k in self.models:
                result['models'].append(k.to_map() if k else None)
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.status is not None:
            result['status'] = self.status
        if self.scene is not None:
            result['scene'] = self.scene
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.id is not None:
            result['id'] = self.id
        if self.desc is not None:
            result['desc'] = self.desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apps') is not None:
            self.apps = m.get('apps')
        if m.get('appGroupName') is not None:
            self.app_group_name = m.get('appGroupName')
        self.models = []
        if m.get('models') is not None:
            for k in m.get('models'):
                temp_model = ListDeployedAlgorithmModelsResponseBodyResultModels()
                self.models.append(temp_model.from_map(k))
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        return self


class ListDeployedAlgorithmModelsResponseBody(TeaModel):
    def __init__(
        self,
        result: List[ListDeployedAlgorithmModelsResponseBodyResult] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListDeployedAlgorithmModelsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListDeployedAlgorithmModelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDeployedAlgorithmModelsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDeployedAlgorithmModelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFirstRanksResponseBodyResultMeta(TeaModel):
    def __init__(
        self,
        arg: str = None,
        attribute: str = None,
        weight: int = None,
    ):
        self.arg = arg
        self.attribute = attribute
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arg is not None:
            result['arg'] = self.arg
        if self.attribute is not None:
            result['attribute'] = self.attribute
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arg') is not None:
            self.arg = m.get('arg')
        if m.get('attribute') is not None:
            self.attribute = m.get('attribute')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class ListFirstRanksResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        active: bool = None,
        description: str = None,
        updated: int = None,
        name: str = None,
        meta: List[ListFirstRanksResponseBodyResultMeta] = None,
    ):
        self.created = created
        self.active = active
        self.description = description
        self.updated = updated
        self.name = name
        self.meta = meta

    def validate(self):
        if self.meta:
            for k in self.meta:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.active is not None:
            result['active'] = self.active
        if self.description is not None:
            result['description'] = self.description
        if self.updated is not None:
            result['updated'] = self.updated
        if self.name is not None:
            result['name'] = self.name
        result['meta'] = []
        if self.meta is not None:
            for k in self.meta:
                result['meta'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.meta = []
        if m.get('meta') is not None:
            for k in m.get('meta'):
                temp_model = ListFirstRanksResponseBodyResultMeta()
                self.meta.append(temp_model.from_map(k))
        return self


class ListFirstRanksResponseBody(TeaModel):
    def __init__(
        self,
        result: List[ListFirstRanksResponseBodyResult] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListFirstRanksResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListFirstRanksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListFirstRanksResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListFirstRanksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInterventionDictionariesRequest(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        page_number: int = None,
        types: str = None,
    ):
        self.page_size = page_size
        self.page_number = page_number
        self.types = types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.types is not None:
            result['types'] = self.types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('types') is not None:
            self.types = m.get('types')
        return self


class ListInterventionDictionariesResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        type: str = None,
        analyzer: str = None,
        name: str = None,
        updated: int = None,
        id: int = None,
    ):
        self.created = created
        self.type = type
        self.analyzer = analyzer
        self.name = name
        self.updated = updated
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.type is not None:
            result['type'] = self.type
        if self.analyzer is not None:
            result['analyzer'] = self.analyzer
        if self.name is not None:
            result['name'] = self.name
        if self.updated is not None:
            result['updated'] = self.updated
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('analyzer') is not None:
            self.analyzer = m.get('analyzer')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class ListInterventionDictionariesResponseBody(TeaModel):
    def __init__(
        self,
        result: List[ListInterventionDictionariesResponseBodyResult] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.result = result
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListInterventionDictionariesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListInterventionDictionariesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListInterventionDictionariesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListInterventionDictionariesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInterventionDictionaryEntriesRequest(TeaModel):
    def __init__(
        self,
        word: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.word = word
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.word is not None:
            result['word'] = self.word
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('word') is not None:
            self.word = m.get('word')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListInterventionDictionaryEntriesResponseBodyResultTokens(TeaModel):
    def __init__(
        self,
        tag_label: str = None,
        tag: str = None,
        token: str = None,
        order: int = None,
    ):
        self.tag_label = tag_label
        self.tag = tag
        self.token = token
        self.order = order

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_label is not None:
            result['tagLabel'] = self.tag_label
        if self.tag is not None:
            result['tag'] = self.tag
        if self.token is not None:
            result['token'] = self.token
        if self.order is not None:
            result['order'] = self.order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagLabel') is not None:
            self.tag_label = m.get('tagLabel')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('token') is not None:
            self.token = m.get('token')
        if m.get('order') is not None:
            self.order = m.get('order')
        return self


class ListInterventionDictionaryEntriesResponseBodyResult(TeaModel):
    def __init__(
        self,
        cmd: str = None,
        created: int = None,
        word: str = None,
        tokens: List[ListInterventionDictionaryEntriesResponseBodyResultTokens] = None,
        relevance: Dict[str, Any] = None,
        status: str = None,
        updated: int = None,
    ):
        self.cmd = cmd
        self.created = created
        self.word = word
        self.tokens = tokens
        self.relevance = relevance
        self.status = status
        self.updated = updated

    def validate(self):
        if self.tokens:
            for k in self.tokens:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cmd is not None:
            result['cmd'] = self.cmd
        if self.created is not None:
            result['created'] = self.created
        if self.word is not None:
            result['word'] = self.word
        result['tokens'] = []
        if self.tokens is not None:
            for k in self.tokens:
                result['tokens'].append(k.to_map() if k else None)
        if self.relevance is not None:
            result['relevance'] = self.relevance
        if self.status is not None:
            result['status'] = self.status
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cmd') is not None:
            self.cmd = m.get('cmd')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('word') is not None:
            self.word = m.get('word')
        self.tokens = []
        if m.get('tokens') is not None:
            for k in m.get('tokens'):
                temp_model = ListInterventionDictionaryEntriesResponseBodyResultTokens()
                self.tokens.append(temp_model.from_map(k))
        if m.get('relevance') is not None:
            self.relevance = m.get('relevance')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class ListInterventionDictionaryEntriesResponseBody(TeaModel):
    def __init__(
        self,
        result: List[ListInterventionDictionaryEntriesResponseBodyResult] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.result = result
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListInterventionDictionaryEntriesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListInterventionDictionaryEntriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListInterventionDictionaryEntriesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListInterventionDictionaryEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInterventionDictionaryNerResultsRequest(TeaModel):
    def __init__(
        self,
        query: str = None,
    ):
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query is not None:
            result['query'] = self.query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('query') is not None:
            self.query = m.get('query')
        return self


class ListInterventionDictionaryNerResultsResponseBodyResult(TeaModel):
    def __init__(
        self,
        tag_label: str = None,
        tag: str = None,
        token: str = None,
        order: int = None,
    ):
        self.tag_label = tag_label
        self.tag = tag
        self.token = token
        self.order = order

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_label is not None:
            result['tagLabel'] = self.tag_label
        if self.tag is not None:
            result['tag'] = self.tag
        if self.token is not None:
            result['token'] = self.token
        if self.order is not None:
            result['order'] = self.order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagLabel') is not None:
            self.tag_label = m.get('tagLabel')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('token') is not None:
            self.token = m.get('token')
        if m.get('order') is not None:
            self.order = m.get('order')
        return self


class ListInterventionDictionaryNerResultsResponseBody(TeaModel):
    def __init__(
        self,
        result: List[ListInterventionDictionaryNerResultsResponseBodyResult] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListInterventionDictionaryNerResultsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListInterventionDictionaryNerResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListInterventionDictionaryNerResultsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListInterventionDictionaryNerResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInterventionDictionaryRelatedEntitiesResponseBody(TeaModel):
    def __init__(
        self,
        result: List[Dict[str, Any]] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListInterventionDictionaryRelatedEntitiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListInterventionDictionaryRelatedEntitiesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListInterventionDictionaryRelatedEntitiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListModelsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        type: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListModelsResponseBody(TeaModel):
    def __init__(
        self,
        result: List[Dict[str, Any]] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListModelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListModelsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListModelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQueryProcessorNersRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
    ):
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        return self


class ListQueryProcessorNersResponseBodyResult(TeaModel):
    def __init__(
        self,
        label: str = None,
        tag: str = None,
        order: int = None,
        priority: str = None,
    ):
        self.label = label
        self.tag = tag
        self.order = order
        self.priority = priority

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['label'] = self.label
        if self.tag is not None:
            result['tag'] = self.tag
        if self.order is not None:
            result['order'] = self.order
        if self.priority is not None:
            result['priority'] = self.priority
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        return self


class ListQueryProcessorNersResponseBody(TeaModel):
    def __init__(
        self,
        result: List[ListQueryProcessorNersResponseBodyResult] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListQueryProcessorNersResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListQueryProcessorNersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListQueryProcessorNersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListQueryProcessorNersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQueryProcessorsRequest(TeaModel):
    def __init__(
        self,
        is_active: int = None,
    ):
        self.is_active = is_active

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_active is not None:
            result['isActive'] = self.is_active
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isActive') is not None:
            self.is_active = m.get('isActive')
        return self


class ListQueryProcessorsResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        active: bool = None,
        domain: str = None,
        indexes: List[str] = None,
        processors: List[Dict[str, Any]] = None,
        updated: int = None,
        name: str = None,
    ):
        self.created = created
        self.active = active
        self.domain = domain
        self.indexes = indexes
        self.processors = processors
        self.updated = updated
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.active is not None:
            result['active'] = self.active
        if self.domain is not None:
            result['domain'] = self.domain
        if self.indexes is not None:
            result['indexes'] = self.indexes
        if self.processors is not None:
            result['processors'] = self.processors
        if self.updated is not None:
            result['updated'] = self.updated
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('indexes') is not None:
            self.indexes = m.get('indexes')
        if m.get('processors') is not None:
            self.processors = m.get('processors')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListQueryProcessorsResponseBody(TeaModel):
    def __init__(
        self,
        result: List[ListQueryProcessorsResponseBodyResult] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListQueryProcessorsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListQueryProcessorsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListQueryProcessorsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListQueryProcessorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListScheduledTasksRequest(TeaModel):
    def __init__(
        self,
        type: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.type = type
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListScheduledTasksResponseBody(TeaModel):
    def __init__(
        self,
        result: List[Dict[str, Any]] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.result = result
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListScheduledTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListScheduledTasksResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListScheduledTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSecondRanksResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        active: bool = None,
        is_default: str = None,
        is_sys: str = None,
        description: str = None,
        updated: int = None,
        name: str = None,
        meta: str = None,
        id: str = None,
    ):
        self.created = created
        self.active = active
        self.is_default = is_default
        self.is_sys = is_sys
        self.description = description
        self.updated = updated
        self.name = name
        self.meta = meta
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.active is not None:
            result['active'] = self.active
        if self.is_default is not None:
            result['isDefault'] = self.is_default
        if self.is_sys is not None:
            result['isSys'] = self.is_sys
        if self.description is not None:
            result['description'] = self.description
        if self.updated is not None:
            result['updated'] = self.updated
        if self.name is not None:
            result['name'] = self.name
        if self.meta is not None:
            result['meta'] = self.meta
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('isDefault') is not None:
            self.is_default = m.get('isDefault')
        if m.get('isSys') is not None:
            self.is_sys = m.get('isSys')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class ListSecondRanksResponseBody(TeaModel):
    def __init__(
        self,
        result: List[ListSecondRanksResponseBodyResult] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.result = result
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListSecondRanksResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListSecondRanksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSecondRanksResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListSecondRanksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSlowQueryCategoriesResponseBodyResult(TeaModel):
    def __init__(
        self,
        start: int = None,
        analyze_status: str = None,
        end: int = None,
    ):
        self.start = start
        self.analyze_status = analyze_status
        self.end = end

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start is not None:
            result['start'] = self.start
        if self.analyze_status is not None:
            result['analyzeStatus'] = self.analyze_status
        if self.end is not None:
            result['end'] = self.end
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('start') is not None:
            self.start = m.get('start')
        if m.get('analyzeStatus') is not None:
            self.analyze_status = m.get('analyzeStatus')
        if m.get('end') is not None:
            self.end = m.get('end')
        return self


class ListSlowQueryCategoriesResponseBody(TeaModel):
    def __init__(
        self,
        result: ListSlowQueryCategoriesResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = ListSlowQueryCategoriesResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListSlowQueryCategoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSlowQueryCategoriesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListSlowQueryCategoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSlowQueryQueriesResponseBodyResult(TeaModel):
    def __init__(
        self,
        index: int = None,
        app_query: str = None,
        start: int = None,
        end: int = None,
    ):
        self.index = index
        self.app_query = app_query
        self.start = start
        self.end = end

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['index'] = self.index
        if self.app_query is not None:
            result['appQuery'] = self.app_query
        if self.start is not None:
            result['start'] = self.start
        if self.end is not None:
            result['end'] = self.end
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('appQuery') is not None:
            self.app_query = m.get('appQuery')
        if m.get('start') is not None:
            self.start = m.get('start')
        if m.get('end') is not None:
            self.end = m.get('end')
        return self


class ListSlowQueryQueriesResponseBody(TeaModel):
    def __init__(
        self,
        result: ListSlowQueryQueriesResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = ListSlowQueryQueriesResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListSlowQueryQueriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSlowQueryQueriesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListSlowQueryQueriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSortExpressionsResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        active: bool = None,
        description: str = None,
        updated: int = None,
        name: str = None,
    ):
        self.created = created
        self.active = active
        self.description = description
        self.updated = updated
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.active is not None:
            result['active'] = self.active
        if self.description is not None:
            result['description'] = self.description
        if self.updated is not None:
            result['updated'] = self.updated
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListSortExpressionsResponseBody(TeaModel):
    def __init__(
        self,
        result: List[ListSortExpressionsResponseBodyResult] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListSortExpressionsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListSortExpressionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSortExpressionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListSortExpressionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSortScriptsResponseBodyResult(TeaModel):
    def __init__(
        self,
        type: str = None,
        scope: str = None,
        create_time: str = None,
        status: str = None,
        modify_time: str = None,
        script_name: str = None,
    ):
        self.type = type
        self.scope = scope
        self.create_time = create_time
        self.status = status
        self.modify_time = modify_time
        self.script_name = script_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.scope is not None:
            result['scope'] = self.scope
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.status is not None:
            result['status'] = self.status
        if self.modify_time is not None:
            result['modifyTime'] = self.modify_time
        if self.script_name is not None:
            result['scriptName'] = self.script_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')
        if m.get('scriptName') is not None:
            self.script_name = m.get('scriptName')
        return self


class ListSortScriptsResponseBody(TeaModel):
    def __init__(
        self,
        result: List[ListSortScriptsResponseBodyResult] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListSortScriptsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListSortScriptsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSortScriptsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListSortScriptsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListStatisticLogsRequest(TeaModel):
    def __init__(
        self,
        start_time: int = None,
        stop_time: int = None,
        page_number: int = None,
        page_size: int = None,
        query: str = None,
        sort_by: str = None,
        distinct: bool = None,
        columns: str = None,
    ):
        self.start_time = start_time
        self.stop_time = stop_time
        self.page_number = page_number
        self.page_size = page_size
        self.query = query
        self.sort_by = sort_by
        self.distinct = distinct
        self.columns = columns

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.stop_time is not None:
            result['stopTime'] = self.stop_time
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.query is not None:
            result['query'] = self.query
        if self.sort_by is not None:
            result['sortBy'] = self.sort_by
        if self.distinct is not None:
            result['distinct'] = self.distinct
        if self.columns is not None:
            result['columns'] = self.columns
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('stopTime') is not None:
            self.stop_time = m.get('stopTime')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('sortBy') is not None:
            self.sort_by = m.get('sortBy')
        if m.get('distinct') is not None:
            self.distinct = m.get('distinct')
        if m.get('columns') is not None:
            self.columns = m.get('columns')
        return self


class ListStatisticLogsResponseBody(TeaModel):
    def __init__(
        self,
        result: List[Dict[str, Any]] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.result = result
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListStatisticLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListStatisticLogsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListStatisticLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListStatisticReportRequest(TeaModel):
    def __init__(
        self,
        start_time: int = None,
        end_time: int = None,
        page_number: int = None,
        page_size: int = None,
        columns: str = None,
        query: str = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size
        self.columns = columns
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.columns is not None:
            result['columns'] = self.columns
        if self.query is not None:
            result['query'] = self.query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('columns') is not None:
            self.columns = m.get('columns')
        if m.get('query') is not None:
            self.query = m.get('query')
        return self


class ListStatisticReportResponseBody(TeaModel):
    def __init__(
        self,
        result: List[Dict[str, Any]] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.result = result
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListStatisticReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListStatisticReportResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListStatisticReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserAnalyzerEntriesRequest(TeaModel):
    def __init__(
        self,
        word: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.word = word
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.word is not None:
            result['word'] = self.word
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('word') is not None:
            self.word = m.get('word')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListUserAnalyzerEntriesResponseBody(TeaModel):
    def __init__(
        self,
        result: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListUserAnalyzerEntriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListUserAnalyzerEntriesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListUserAnalyzerEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserAnalyzersRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListUserAnalyzersResponseBodyResultDicts(TeaModel):
    def __init__(
        self,
        created: int = None,
        entries_count: int = None,
        type: str = None,
        entries_limit: int = None,
        available: bool = None,
        updated: int = None,
        id: str = None,
    ):
        self.created = created
        self.entries_count = entries_count
        self.type = type
        self.entries_limit = entries_limit
        self.available = available
        self.updated = updated
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.entries_count is not None:
            result['entriesCount'] = self.entries_count
        if self.type is not None:
            result['type'] = self.type
        if self.entries_limit is not None:
            result['entriesLimit'] = self.entries_limit
        if self.available is not None:
            result['available'] = self.available
        if self.updated is not None:
            result['updated'] = self.updated
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('entriesCount') is not None:
            self.entries_count = m.get('entriesCount')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('entriesLimit') is not None:
            self.entries_limit = m.get('entriesLimit')
        if m.get('available') is not None:
            self.available = m.get('available')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class ListUserAnalyzersResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        available: bool = None,
        dicts: List[ListUserAnalyzersResponseBodyResultDicts] = None,
        name: str = None,
        updated: int = None,
        id: str = None,
        business: str = None,
    ):
        self.created = created
        self.available = available
        self.dicts = dicts
        self.name = name
        self.updated = updated
        self.id = id
        self.business = business

    def validate(self):
        if self.dicts:
            for k in self.dicts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.available is not None:
            result['available'] = self.available
        result['dicts'] = []
        if self.dicts is not None:
            for k in self.dicts:
                result['dicts'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.updated is not None:
            result['updated'] = self.updated
        if self.id is not None:
            result['id'] = self.id
        if self.business is not None:
            result['business'] = self.business
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('available') is not None:
            self.available = m.get('available')
        self.dicts = []
        if m.get('dicts') is not None:
            for k in m.get('dicts'):
                temp_model = ListUserAnalyzersResponseBodyResultDicts()
                self.dicts.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('business') is not None:
            self.business = m.get('business')
        return self


class ListUserAnalyzersResponseBody(TeaModel):
    def __init__(
        self,
        result: List[ListUserAnalyzersResponseBodyResult] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.result = result
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListUserAnalyzersResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListUserAnalyzersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListUserAnalyzersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListUserAnalyzersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAppGroupResponseBodyResultQuota(TeaModel):
    def __init__(
        self,
        spec: str = None,
        doc_size: int = None,
        compute_resource: int = None,
    ):
        self.spec = spec
        self.doc_size = doc_size
        self.compute_resource = compute_resource

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spec is not None:
            result['spec'] = self.spec
        if self.doc_size is not None:
            result['docSize'] = self.doc_size
        if self.compute_resource is not None:
            result['computeResource'] = self.compute_resource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('docSize') is not None:
            self.doc_size = m.get('docSize')
        if m.get('computeResource') is not None:
            self.compute_resource = m.get('computeResource')
        return self


class ModifyAppGroupResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        current_version: str = None,
        pending_second_rank_algo_deployment_id: int = None,
        lock_mode: str = None,
        updated: int = None,
        id: str = None,
        charge_type: str = None,
        has_pending_quota_review_task: int = None,
        second_rank_algo_deployment_id: int = None,
        quota: ModifyAppGroupResponseBodyResultQuota = None,
        name: str = None,
        processing_order_id: str = None,
        instance_id: str = None,
        type: str = None,
        charging_way: int = None,
        status: str = None,
        project_id: str = None,
        commodity_code: str = None,
        switched_time: int = None,
        expire_on: str = None,
        domain: str = None,
        description: str = None,
        first_rank_algo_deployment_id: int = None,
        produced: int = None,
        locked_by_expiration: int = None,
    ):
        self.created = created
        self.current_version = current_version
        self.pending_second_rank_algo_deployment_id = pending_second_rank_algo_deployment_id
        self.lock_mode = lock_mode
        self.updated = updated
        self.id = id
        self.charge_type = charge_type
        self.has_pending_quota_review_task = has_pending_quota_review_task
        self.second_rank_algo_deployment_id = second_rank_algo_deployment_id
        self.quota = quota
        self.name = name
        self.processing_order_id = processing_order_id
        self.instance_id = instance_id
        self.type = type
        self.charging_way = charging_way
        self.status = status
        self.project_id = project_id
        self.commodity_code = commodity_code
        self.switched_time = switched_time
        self.expire_on = expire_on
        self.domain = domain
        self.description = description
        self.first_rank_algo_deployment_id = first_rank_algo_deployment_id
        self.produced = produced
        self.locked_by_expiration = locked_by_expiration

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.current_version is not None:
            result['currentVersion'] = self.current_version
        if self.pending_second_rank_algo_deployment_id is not None:
            result['pendingSecondRankAlgoDeploymentId'] = self.pending_second_rank_algo_deployment_id
        if self.lock_mode is not None:
            result['lockMode'] = self.lock_mode
        if self.updated is not None:
            result['updated'] = self.updated
        if self.id is not None:
            result['id'] = self.id
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.has_pending_quota_review_task is not None:
            result['hasPendingQuotaReviewTask'] = self.has_pending_quota_review_task
        if self.second_rank_algo_deployment_id is not None:
            result['secondRankAlgoDeploymentId'] = self.second_rank_algo_deployment_id
        if self.quota is not None:
            result['quota'] = self.quota.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.processing_order_id is not None:
            result['processingOrderId'] = self.processing_order_id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.type is not None:
            result['type'] = self.type
        if self.charging_way is not None:
            result['chargingWay'] = self.charging_way
        if self.status is not None:
            result['status'] = self.status
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.switched_time is not None:
            result['switchedTime'] = self.switched_time
        if self.expire_on is not None:
            result['expireOn'] = self.expire_on
        if self.domain is not None:
            result['domain'] = self.domain
        if self.description is not None:
            result['description'] = self.description
        if self.first_rank_algo_deployment_id is not None:
            result['firstRankAlgoDeploymentId'] = self.first_rank_algo_deployment_id
        if self.produced is not None:
            result['produced'] = self.produced
        if self.locked_by_expiration is not None:
            result['lockedByExpiration'] = self.locked_by_expiration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('currentVersion') is not None:
            self.current_version = m.get('currentVersion')
        if m.get('pendingSecondRankAlgoDeploymentId') is not None:
            self.pending_second_rank_algo_deployment_id = m.get('pendingSecondRankAlgoDeploymentId')
        if m.get('lockMode') is not None:
            self.lock_mode = m.get('lockMode')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('hasPendingQuotaReviewTask') is not None:
            self.has_pending_quota_review_task = m.get('hasPendingQuotaReviewTask')
        if m.get('secondRankAlgoDeploymentId') is not None:
            self.second_rank_algo_deployment_id = m.get('secondRankAlgoDeploymentId')
        if m.get('quota') is not None:
            temp_model = ModifyAppGroupResponseBodyResultQuota()
            self.quota = temp_model.from_map(m['quota'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('processingOrderId') is not None:
            self.processing_order_id = m.get('processingOrderId')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('chargingWay') is not None:
            self.charging_way = m.get('chargingWay')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('switchedTime') is not None:
            self.switched_time = m.get('switchedTime')
        if m.get('expireOn') is not None:
            self.expire_on = m.get('expireOn')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('firstRankAlgoDeploymentId') is not None:
            self.first_rank_algo_deployment_id = m.get('firstRankAlgoDeploymentId')
        if m.get('produced') is not None:
            self.produced = m.get('produced')
        if m.get('lockedByExpiration') is not None:
            self.locked_by_expiration = m.get('lockedByExpiration')
        return self


class ModifyAppGroupResponseBody(TeaModel):
    def __init__(
        self,
        result: ModifyAppGroupResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = ModifyAppGroupResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ModifyAppGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyAppGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyAppGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAppGroupQuotaResponseBodyResultQuota(TeaModel):
    def __init__(
        self,
        spec: str = None,
        doc_size: int = None,
        compute_resource: int = None,
    ):
        self.spec = spec
        self.doc_size = doc_size
        self.compute_resource = compute_resource

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spec is not None:
            result['spec'] = self.spec
        if self.doc_size is not None:
            result['docSize'] = self.doc_size
        if self.compute_resource is not None:
            result['computeResource'] = self.compute_resource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('docSize') is not None:
            self.doc_size = m.get('docSize')
        if m.get('computeResource') is not None:
            self.compute_resource = m.get('computeResource')
        return self


class ModifyAppGroupQuotaResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        current_version: str = None,
        pending_second_rank_algo_deployment_id: int = None,
        lock_mode: str = None,
        updated: int = None,
        id: str = None,
        charge_type: str = None,
        has_pending_quota_review_task: int = None,
        second_rank_algo_deployment_id: int = None,
        quota: ModifyAppGroupQuotaResponseBodyResultQuota = None,
        name: str = None,
        processing_order_id: str = None,
        instance_id: str = None,
        type: str = None,
        charging_way: int = None,
        status: str = None,
        project_id: str = None,
        commodity_code: str = None,
        switched_time: int = None,
        expire_on: str = None,
        description: str = None,
        first_rank_algo_deployment_id: int = None,
        locked_by_expiration: int = None,
        produced: int = None,
    ):
        self.created = created
        self.current_version = current_version
        self.pending_second_rank_algo_deployment_id = pending_second_rank_algo_deployment_id
        self.lock_mode = lock_mode
        self.updated = updated
        self.id = id
        self.charge_type = charge_type
        self.has_pending_quota_review_task = has_pending_quota_review_task
        self.second_rank_algo_deployment_id = second_rank_algo_deployment_id
        self.quota = quota
        self.name = name
        self.processing_order_id = processing_order_id
        self.instance_id = instance_id
        self.type = type
        self.charging_way = charging_way
        self.status = status
        self.project_id = project_id
        self.commodity_code = commodity_code
        self.switched_time = switched_time
        self.expire_on = expire_on
        self.description = description
        self.first_rank_algo_deployment_id = first_rank_algo_deployment_id
        self.locked_by_expiration = locked_by_expiration
        self.produced = produced

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.current_version is not None:
            result['currentVersion'] = self.current_version
        if self.pending_second_rank_algo_deployment_id is not None:
            result['pendingSecondRankAlgoDeploymentId'] = self.pending_second_rank_algo_deployment_id
        if self.lock_mode is not None:
            result['lockMode'] = self.lock_mode
        if self.updated is not None:
            result['updated'] = self.updated
        if self.id is not None:
            result['id'] = self.id
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.has_pending_quota_review_task is not None:
            result['hasPendingQuotaReviewTask'] = self.has_pending_quota_review_task
        if self.second_rank_algo_deployment_id is not None:
            result['secondRankAlgoDeploymentId'] = self.second_rank_algo_deployment_id
        if self.quota is not None:
            result['quota'] = self.quota.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.processing_order_id is not None:
            result['processingOrderId'] = self.processing_order_id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.type is not None:
            result['type'] = self.type
        if self.charging_way is not None:
            result['chargingWay'] = self.charging_way
        if self.status is not None:
            result['status'] = self.status
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.switched_time is not None:
            result['switchedTime'] = self.switched_time
        if self.expire_on is not None:
            result['expireOn'] = self.expire_on
        if self.description is not None:
            result['description'] = self.description
        if self.first_rank_algo_deployment_id is not None:
            result['firstRankAlgoDeploymentId'] = self.first_rank_algo_deployment_id
        if self.locked_by_expiration is not None:
            result['lockedByExpiration'] = self.locked_by_expiration
        if self.produced is not None:
            result['produced'] = self.produced
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('currentVersion') is not None:
            self.current_version = m.get('currentVersion')
        if m.get('pendingSecondRankAlgoDeploymentId') is not None:
            self.pending_second_rank_algo_deployment_id = m.get('pendingSecondRankAlgoDeploymentId')
        if m.get('lockMode') is not None:
            self.lock_mode = m.get('lockMode')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('hasPendingQuotaReviewTask') is not None:
            self.has_pending_quota_review_task = m.get('hasPendingQuotaReviewTask')
        if m.get('secondRankAlgoDeploymentId') is not None:
            self.second_rank_algo_deployment_id = m.get('secondRankAlgoDeploymentId')
        if m.get('quota') is not None:
            temp_model = ModifyAppGroupQuotaResponseBodyResultQuota()
            self.quota = temp_model.from_map(m['quota'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('processingOrderId') is not None:
            self.processing_order_id = m.get('processingOrderId')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('chargingWay') is not None:
            self.charging_way = m.get('chargingWay')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('switchedTime') is not None:
            self.switched_time = m.get('switchedTime')
        if m.get('expireOn') is not None:
            self.expire_on = m.get('expireOn')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('firstRankAlgoDeploymentId') is not None:
            self.first_rank_algo_deployment_id = m.get('firstRankAlgoDeploymentId')
        if m.get('lockedByExpiration') is not None:
            self.locked_by_expiration = m.get('lockedByExpiration')
        if m.get('produced') is not None:
            self.produced = m.get('produced')
        return self


class ModifyAppGroupQuotaResponseBody(TeaModel):
    def __init__(
        self,
        result: ModifyAppGroupQuotaResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = ModifyAppGroupQuotaResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ModifyAppGroupQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyAppGroupQuotaResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyAppGroupQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyFirstRankRequest(TeaModel):
    def __init__(
        self,
        dry_run: bool = None,
    ):
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class ModifyFirstRankResponseBodyResultMeta(TeaModel):
    def __init__(
        self,
        arg: str = None,
        attribute: str = None,
        weight: float = None,
    ):
        self.arg = arg
        self.attribute = attribute
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arg is not None:
            result['arg'] = self.arg
        if self.attribute is not None:
            result['attribute'] = self.attribute
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arg') is not None:
            self.arg = m.get('arg')
        if m.get('attribute') is not None:
            self.attribute = m.get('attribute')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class ModifyFirstRankResponseBodyResult(TeaModel):
    def __init__(
        self,
        active: bool = None,
        description: str = None,
        name: str = None,
        meta: List[ModifyFirstRankResponseBodyResultMeta] = None,
    ):
        self.active = active
        self.description = description
        self.name = name
        self.meta = meta

    def validate(self):
        if self.meta:
            for k in self.meta:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        result['meta'] = []
        if self.meta is not None:
            for k in self.meta:
                result['meta'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.meta = []
        if m.get('meta') is not None:
            for k in m.get('meta'):
                temp_model = ModifyFirstRankResponseBodyResultMeta()
                self.meta.append(temp_model.from_map(k))
        return self


class ModifyFirstRankResponseBody(TeaModel):
    def __init__(
        self,
        result: ModifyFirstRankResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = ModifyFirstRankResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ModifyFirstRankResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyFirstRankResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyFirstRankResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyModelResponseBody(TeaModel):
    def __init__(
        self,
        result: str = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ModifyModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyModelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyQueryProcessorRequest(TeaModel):
    def __init__(
        self,
        dry_run: bool = None,
    ):
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class ModifyQueryProcessorResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        active: bool = None,
        domain: str = None,
        indexes: List[str] = None,
        processors: List[Dict[str, Any]] = None,
        updated: int = None,
        name: str = None,
    ):
        self.created = created
        self.active = active
        self.domain = domain
        self.indexes = indexes
        self.processors = processors
        self.updated = updated
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.active is not None:
            result['active'] = self.active
        if self.domain is not None:
            result['domain'] = self.domain
        if self.indexes is not None:
            result['indexes'] = self.indexes
        if self.processors is not None:
            result['processors'] = self.processors
        if self.updated is not None:
            result['updated'] = self.updated
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('indexes') is not None:
            self.indexes = m.get('indexes')
        if m.get('processors') is not None:
            self.processors = m.get('processors')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ModifyQueryProcessorResponseBody(TeaModel):
    def __init__(
        self,
        result: ModifyQueryProcessorResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = ModifyQueryProcessorResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ModifyQueryProcessorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyQueryProcessorResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyQueryProcessorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyScheduledTaskResponseBody(TeaModel):
    def __init__(
        self,
        result: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ModifyScheduledTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyScheduledTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyScheduledTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySecondRankRequest(TeaModel):
    def __init__(
        self,
        dry_run: bool = None,
    ):
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class ModifySecondRankResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        active: bool = None,
        is_default: str = None,
        is_sys: str = None,
        description: str = None,
        updated: int = None,
        name: str = None,
        meta: str = None,
        id: str = None,
    ):
        self.created = created
        self.active = active
        self.is_default = is_default
        self.is_sys = is_sys
        self.description = description
        self.updated = updated
        self.name = name
        self.meta = meta
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.active is not None:
            result['active'] = self.active
        if self.is_default is not None:
            result['isDefault'] = self.is_default
        if self.is_sys is not None:
            result['isSys'] = self.is_sys
        if self.description is not None:
            result['description'] = self.description
        if self.updated is not None:
            result['updated'] = self.updated
        if self.name is not None:
            result['name'] = self.name
        if self.meta is not None:
            result['meta'] = self.meta
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('isDefault') is not None:
            self.is_default = m.get('isDefault')
        if m.get('isSys') is not None:
            self.is_sys = m.get('isSys')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class ModifySecondRankResponseBody(TeaModel):
    def __init__(
        self,
        result: ModifySecondRankResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = ModifySecondRankResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ModifySecondRankResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifySecondRankResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifySecondRankResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PreviewModelRequest(TeaModel):
    def __init__(
        self,
        query: str = None,
    ):
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query is not None:
            result['query'] = self.query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('query') is not None:
            self.query = m.get('query')
        return self


class PreviewModelResponseBody(TeaModel):
    def __init__(
        self,
        result: List[Dict[str, Any]] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.result = result
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class PreviewModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PreviewModelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = PreviewModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushInterventionDictionaryEntriesResponseBody(TeaModel):
    def __init__(
        self,
        result: List[str] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class PushInterventionDictionaryEntriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PushInterventionDictionaryEntriesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = PushInterventionDictionaryEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushUserAnalyzerEntriesResponseBody(TeaModel):
    def __init__(
        self,
        result: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PushUserAnalyzerEntriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PushUserAnalyzerEntriesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = PushUserAnalyzerEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RankPreviewQueryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class RankPreviewQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RankPreviewQueryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RankPreviewQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseSortScriptResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ReleaseSortScriptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReleaseSortScriptResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ReleaseSortScriptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveAppResponseBody(TeaModel):
    def __init__(
        self,
        result: List[int] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class RemoveAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveAppResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveAppGroupResponseBody(TeaModel):
    def __init__(
        self,
        result: List[int] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class RemoveAppGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveAppGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveAppGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveDataCollectionResponseBody(TeaModel):
    def __init__(
        self,
        result: str = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class RemoveDataCollectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveDataCollectionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveDataCollectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveFirstRankResponseBodyResultMeta(TeaModel):
    def __init__(
        self,
        arg: str = None,
        attribute: str = None,
        weight: float = None,
    ):
        self.arg = arg
        self.attribute = attribute
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arg is not None:
            result['arg'] = self.arg
        if self.attribute is not None:
            result['attribute'] = self.attribute
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arg') is not None:
            self.arg = m.get('arg')
        if m.get('attribute') is not None:
            self.attribute = m.get('attribute')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class RemoveFirstRankResponseBodyResult(TeaModel):
    def __init__(
        self,
        active: bool = None,
        description: str = None,
        name: str = None,
        meta: List[RemoveFirstRankResponseBodyResultMeta] = None,
    ):
        self.active = active
        self.description = description
        self.name = name
        self.meta = meta

    def validate(self):
        if self.meta:
            for k in self.meta:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        result['meta'] = []
        if self.meta is not None:
            for k in self.meta:
                result['meta'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.meta = []
        if m.get('meta') is not None:
            for k in m.get('meta'):
                temp_model = RemoveFirstRankResponseBodyResultMeta()
                self.meta.append(temp_model.from_map(k))
        return self


class RemoveFirstRankResponseBody(TeaModel):
    def __init__(
        self,
        result: RemoveFirstRankResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = RemoveFirstRankResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class RemoveFirstRankResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveFirstRankResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveFirstRankResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveInterventionDictionaryResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: str = None,
        type: str = None,
        analyzer: str = None,
        updated: str = None,
        name: str = None,
    ):
        self.created = created
        self.type = type
        self.analyzer = analyzer
        self.updated = updated
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.type is not None:
            result['type'] = self.type
        if self.analyzer is not None:
            result['analyzer'] = self.analyzer
        if self.updated is not None:
            result['updated'] = self.updated
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('analyzer') is not None:
            self.analyzer = m.get('analyzer')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class RemoveInterventionDictionaryResponseBody(TeaModel):
    def __init__(
        self,
        result: RemoveInterventionDictionaryResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = RemoveInterventionDictionaryResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class RemoveInterventionDictionaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveInterventionDictionaryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveInterventionDictionaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveQueryProcessorResponseBody(TeaModel):
    def __init__(
        self,
        result: str = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class RemoveQueryProcessorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveQueryProcessorResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveQueryProcessorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveScheduledTaskResponseBody(TeaModel):
    def __init__(
        self,
        result: List[int] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class RemoveScheduledTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveScheduledTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveScheduledTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveSecondRankResponseBody(TeaModel):
    def __init__(
        self,
        result: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class RemoveSecondRankResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveSecondRankResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveSecondRankResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveUserAnalyzerResponseBody(TeaModel):
    def __init__(
        self,
        result: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class RemoveUserAnalyzerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveUserAnalyzerResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveUserAnalyzerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewAppGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class RenewAppGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RenewAppGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RenewAppGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReplaceAppGroupCommodityCodeResponseBodyResultQuota(TeaModel):
    def __init__(
        self,
        spec: str = None,
        doc_size: int = None,
        compute_resource: int = None,
    ):
        self.spec = spec
        self.doc_size = doc_size
        self.compute_resource = compute_resource

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spec is not None:
            result['spec'] = self.spec
        if self.doc_size is not None:
            result['docSize'] = self.doc_size
        if self.compute_resource is not None:
            result['computeResource'] = self.compute_resource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('docSize') is not None:
            self.doc_size = m.get('docSize')
        if m.get('computeResource') is not None:
            self.compute_resource = m.get('computeResource')
        return self


class ReplaceAppGroupCommodityCodeResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        current_version: str = None,
        pending_second_rank_algo_deployment_id: int = None,
        lock_mode: str = None,
        updated: int = None,
        id: str = None,
        charge_type: str = None,
        has_pending_quota_review_task: int = None,
        second_rank_algo_deployment_id: int = None,
        versions: List[str] = None,
        quota: ReplaceAppGroupCommodityCodeResponseBodyResultQuota = None,
        name: str = None,
        processing_order_id: str = None,
        instance_id: str = None,
        type: str = None,
        charging_way: int = None,
        status: str = None,
        project_id: str = None,
        commodity_code: str = None,
        switched_time: int = None,
        expire_on: str = None,
        description: str = None,
        first_rank_algo_deployment_id: int = None,
        produced: int = None,
        locked_by_expiration: int = None,
    ):
        self.created = created
        self.current_version = current_version
        self.pending_second_rank_algo_deployment_id = pending_second_rank_algo_deployment_id
        self.lock_mode = lock_mode
        self.updated = updated
        self.id = id
        self.charge_type = charge_type
        self.has_pending_quota_review_task = has_pending_quota_review_task
        self.second_rank_algo_deployment_id = second_rank_algo_deployment_id
        self.versions = versions
        self.quota = quota
        self.name = name
        self.processing_order_id = processing_order_id
        self.instance_id = instance_id
        self.type = type
        self.charging_way = charging_way
        self.status = status
        self.project_id = project_id
        self.commodity_code = commodity_code
        self.switched_time = switched_time
        self.expire_on = expire_on
        self.description = description
        self.first_rank_algo_deployment_id = first_rank_algo_deployment_id
        self.produced = produced
        self.locked_by_expiration = locked_by_expiration

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.current_version is not None:
            result['currentVersion'] = self.current_version
        if self.pending_second_rank_algo_deployment_id is not None:
            result['pendingSecondRankAlgoDeploymentId'] = self.pending_second_rank_algo_deployment_id
        if self.lock_mode is not None:
            result['lockMode'] = self.lock_mode
        if self.updated is not None:
            result['updated'] = self.updated
        if self.id is not None:
            result['id'] = self.id
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.has_pending_quota_review_task is not None:
            result['hasPendingQuotaReviewTask'] = self.has_pending_quota_review_task
        if self.second_rank_algo_deployment_id is not None:
            result['secondRankAlgoDeploymentId'] = self.second_rank_algo_deployment_id
        if self.versions is not None:
            result['versions'] = self.versions
        if self.quota is not None:
            result['quota'] = self.quota.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.processing_order_id is not None:
            result['processingOrderId'] = self.processing_order_id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.type is not None:
            result['type'] = self.type
        if self.charging_way is not None:
            result['chargingWay'] = self.charging_way
        if self.status is not None:
            result['status'] = self.status
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.switched_time is not None:
            result['switchedTime'] = self.switched_time
        if self.expire_on is not None:
            result['expireOn'] = self.expire_on
        if self.description is not None:
            result['description'] = self.description
        if self.first_rank_algo_deployment_id is not None:
            result['firstRankAlgoDeploymentId'] = self.first_rank_algo_deployment_id
        if self.produced is not None:
            result['produced'] = self.produced
        if self.locked_by_expiration is not None:
            result['lockedByExpiration'] = self.locked_by_expiration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('currentVersion') is not None:
            self.current_version = m.get('currentVersion')
        if m.get('pendingSecondRankAlgoDeploymentId') is not None:
            self.pending_second_rank_algo_deployment_id = m.get('pendingSecondRankAlgoDeploymentId')
        if m.get('lockMode') is not None:
            self.lock_mode = m.get('lockMode')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('hasPendingQuotaReviewTask') is not None:
            self.has_pending_quota_review_task = m.get('hasPendingQuotaReviewTask')
        if m.get('secondRankAlgoDeploymentId') is not None:
            self.second_rank_algo_deployment_id = m.get('secondRankAlgoDeploymentId')
        if m.get('versions') is not None:
            self.versions = m.get('versions')
        if m.get('quota') is not None:
            temp_model = ReplaceAppGroupCommodityCodeResponseBodyResultQuota()
            self.quota = temp_model.from_map(m['quota'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('processingOrderId') is not None:
            self.processing_order_id = m.get('processingOrderId')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('chargingWay') is not None:
            self.charging_way = m.get('chargingWay')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('switchedTime') is not None:
            self.switched_time = m.get('switchedTime')
        if m.get('expireOn') is not None:
            self.expire_on = m.get('expireOn')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('firstRankAlgoDeploymentId') is not None:
            self.first_rank_algo_deployment_id = m.get('firstRankAlgoDeploymentId')
        if m.get('produced') is not None:
            self.produced = m.get('produced')
        if m.get('lockedByExpiration') is not None:
            self.locked_by_expiration = m.get('lockedByExpiration')
        return self


class ReplaceAppGroupCommodityCodeResponseBody(TeaModel):
    def __init__(
        self,
        result: ReplaceAppGroupCommodityCodeResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = ReplaceAppGroupCommodityCodeResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ReplaceAppGroupCommodityCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReplaceAppGroupCommodityCodeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ReplaceAppGroupCommodityCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSortScriptFileResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class SaveSortScriptFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SaveSortScriptFileResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SaveSortScriptFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartSlowQueryAnalyzerResponseBody(TeaModel):
    def __init__(
        self,
        result: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class StartSlowQueryAnalyzerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartSlowQueryAnalyzerResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartSlowQueryAnalyzerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TrainModelResponseBody(TeaModel):
    def __init__(
        self,
        result: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class TrainModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TrainModelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = TrainModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateABTestExperimentResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        params: Dict[str, Any] = None,
        traffic: int = None,
        online: bool = None,
        name: str = None,
        updated: int = None,
        id: str = None,
    ):
        self.created = created
        self.params = params
        self.traffic = traffic
        self.online = online
        self.name = name
        self.updated = updated
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.params is not None:
            result['params'] = self.params
        if self.traffic is not None:
            result['traffic'] = self.traffic
        if self.online is not None:
            result['online'] = self.online
        if self.name is not None:
            result['name'] = self.name
        if self.updated is not None:
            result['updated'] = self.updated
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('params') is not None:
            self.params = m.get('params')
        if m.get('traffic') is not None:
            self.traffic = m.get('traffic')
        if m.get('online') is not None:
            self.online = m.get('online')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class UpdateABTestExperimentResponseBody(TeaModel):
    def __init__(
        self,
        result: UpdateABTestExperimentResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = UpdateABTestExperimentResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateABTestExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateABTestExperimentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateABTestExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateABTestFixedFlowDividersResponseBody(TeaModel):
    def __init__(
        self,
        result: List[str] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateABTestFixedFlowDividersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateABTestFixedFlowDividersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateABTestFixedFlowDividersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateABTestGroupResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        status: int = None,
        updated: int = None,
        name: str = None,
        id: str = None,
    ):
        self.created = created
        self.status = status
        self.updated = updated
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.status is not None:
            result['status'] = self.status
        if self.updated is not None:
            result['updated'] = self.updated
        if self.name is not None:
            result['name'] = self.name
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class UpdateABTestGroupResponseBody(TeaModel):
    def __init__(
        self,
        result: UpdateABTestGroupResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = UpdateABTestGroupResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateABTestGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateABTestGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateABTestGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateABTestSceneResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        params: Dict[str, Any] = None,
        traffic: int = None,
        online: bool = None,
        name: str = None,
        updated: int = None,
        id: str = None,
    ):
        self.created = created
        self.params = params
        self.traffic = traffic
        self.online = online
        self.name = name
        self.updated = updated
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.params is not None:
            result['params'] = self.params
        if self.traffic is not None:
            result['traffic'] = self.traffic
        if self.online is not None:
            result['online'] = self.online
        if self.name is not None:
            result['name'] = self.name
        if self.updated is not None:
            result['updated'] = self.updated
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('params') is not None:
            self.params = m.get('params')
        if m.get('traffic') is not None:
            self.traffic = m.get('traffic')
        if m.get('online') is not None:
            self.online = m.get('online')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class UpdateABTestSceneResponseBody(TeaModel):
    def __init__(
        self,
        result: UpdateABTestSceneResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = UpdateABTestSceneResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateABTestSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateABTestSceneResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateABTestSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFetchFieldsRequest(TeaModel):
    def __init__(
        self,
        dry_run: bool = None,
    ):
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class UpdateFetchFieldsResponseBody(TeaModel):
    def __init__(
        self,
        result: bool = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateFetchFieldsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateFetchFieldsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateFetchFieldsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSummariesRequest(TeaModel):
    def __init__(
        self,
        dry_run: bool = None,
    ):
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class UpdateSummariesResponseBody(TeaModel):
    def __init__(
        self,
        result: bool = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateSummariesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateSummariesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateSummariesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


