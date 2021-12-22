# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class AdaptGameVersionRequest(TeaModel):
    def __init__(
        self,
        frame_rate: str = None,
        resolution: str = None,
        version_id: str = None,
    ):
        # 帧率
        self.frame_rate = frame_rate
        # 分辨率
        self.resolution = resolution
        # 游戏版本ID
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class AdaptGameVersionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        # Id of the task
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class AdaptGameVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AdaptGameVersionResponseBody = None,
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
            temp_model = AdaptGameVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddGameToProjectRequest(TeaModel):
    def __init__(
        self,
        game_id: str = None,
        project_id: str = None,
    ):
        # 游戏iD
        self.game_id = game_id
        # 项目ID
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class AddGameToProjectResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddGameToProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddGameToProjectResponseBody = None,
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
            temp_model = AddGameToProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchDispatchGameSlotRequest(TeaModel):
    def __init__(
        self,
        queue_user_list: str = None,
    ):
        self.queue_user_list = queue_user_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.queue_user_list is not None:
            result['QueueUserList'] = self.queue_user_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QueueUserList') is not None:
            self.queue_user_list = m.get('QueueUserList')
        return self


class BatchDispatchGameSlotResponseBodyQueueResultList(TeaModel):
    def __init__(
        self,
        game_id: str = None,
        game_session: str = None,
        message: str = None,
        queue_code: int = None,
        queue_state: int = None,
        region_name: str = None,
        user_id: str = None,
    ):
        self.game_id = game_id
        self.game_session = game_session
        self.message = message
        self.queue_code = queue_code
        self.queue_state = queue_state
        self.region_name = region_name
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.game_session is not None:
            result['GameSession'] = self.game_session
        if self.message is not None:
            result['Message'] = self.message
        if self.queue_code is not None:
            result['QueueCode'] = self.queue_code
        if self.queue_state is not None:
            result['QueueState'] = self.queue_state
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('GameSession') is not None:
            self.game_session = m.get('GameSession')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('QueueCode') is not None:
            self.queue_code = m.get('QueueCode')
        if m.get('QueueState') is not None:
            self.queue_state = m.get('QueueState')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class BatchDispatchGameSlotResponseBody(TeaModel):
    def __init__(
        self,
        queue_result_list: List[BatchDispatchGameSlotResponseBodyQueueResultList] = None,
        request_id: str = None,
    ):
        self.queue_result_list = queue_result_list
        self.request_id = request_id

    def validate(self):
        if self.queue_result_list:
            for k in self.queue_result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['QueueResultList'] = []
        if self.queue_result_list is not None:
            for k in self.queue_result_list:
                result['QueueResultList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.queue_result_list = []
        if m.get('QueueResultList') is not None:
            for k in m.get('QueueResultList'):
                temp_model = BatchDispatchGameSlotResponseBodyQueueResultList()
                self.queue_result_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchDispatchGameSlotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchDispatchGameSlotResponseBody = None,
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
            temp_model = BatchDispatchGameSlotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchStopGameSessionsRequest(TeaModel):
    def __init__(
        self,
        game_id: str = None,
        project_id: str = None,
        reason: str = None,
        tags: str = None,
        token: str = None,
        track_info: str = None,
    ):
        self.game_id = game_id
        self.project_id = project_id
        self.reason = reason
        self.tags = tags
        self.token = token
        self.track_info = track_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.token is not None:
            result['Token'] = self.token
        if self.track_info is not None:
            result['TrackInfo'] = self.track_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('TrackInfo') is not None:
            self.track_info = m.get('TrackInfo')
        return self


class BatchStopGameSessionsResponseBody(TeaModel):
    def __init__(
        self,
        game_id: str = None,
        message: str = None,
        project_id: str = None,
        queue_state: int = None,
        request_id: str = None,
        success: bool = None,
        track_info: str = None,
    ):
        self.game_id = game_id
        self.message = message
        self.project_id = project_id
        self.queue_state = queue_state
        self.request_id = request_id
        self.success = success
        self.track_info = track_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.message is not None:
            result['Message'] = self.message
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.queue_state is not None:
            result['QueueState'] = self.queue_state
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.track_info is not None:
            result['TrackInfo'] = self.track_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('QueueState') is not None:
            self.queue_state = m.get('QueueState')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TrackInfo') is not None:
            self.track_info = m.get('TrackInfo')
        return self


class BatchStopGameSessionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchStopGameSessionsResponseBody = None,
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
            temp_model = BatchStopGameSessionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloseOrderRequest(TeaModel):
    def __init__(
        self,
        account_domain: str = None,
        buyer_account_id: str = None,
        order_id: str = None,
    ):
        self.account_domain = account_domain
        self.buyer_account_id = buyer_account_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_domain is not None:
            result['AccountDomain'] = self.account_domain
        if self.buyer_account_id is not None:
            result['BuyerAccountId'] = self.buyer_account_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountDomain') is not None:
            self.account_domain = m.get('AccountDomain')
        if m.get('BuyerAccountId') is not None:
            self.buyer_account_id = m.get('BuyerAccountId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CloseOrderResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CloseOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CloseOrderResponseBody = None,
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
            temp_model = CloseOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGameRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        game_name: str = None,
        platform_type: int = None,
    ):
        # 幂等参数，1-64位建议使用uuid
        self.client_token = client_token
        # 游戏名称
        self.game_name = game_name
        # 平台类型
        self.platform_type = platform_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.game_name is not None:
            result['GameName'] = self.game_name
        if self.platform_type is not None:
            result['PlatformType'] = self.platform_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('GameName') is not None:
            self.game_name = m.get('GameName')
        if m.get('PlatformType') is not None:
            self.platform_type = m.get('PlatformType')
        return self


class CreateGameResponseBody(TeaModel):
    def __init__(
        self,
        game_id: str = None,
        request_id: str = None,
    ):
        # 游戏ID
        self.game_id = game_id
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateGameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateGameResponseBody = None,
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
            temp_model = CreateGameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGameDeployWorkflowRequest(TeaModel):
    def __init__(
        self,
        download_type: str = None,
        file_type: str = None,
        frame_rate: str = None,
        game_id: str = None,
        game_version: str = None,
        hash: str = None,
        instance: str = None,
        project_id: str = None,
        resolution: str = None,
        version_name: str = None,
    ):
        self.download_type = download_type
        self.file_type = file_type
        self.frame_rate = frame_rate
        self.game_id = game_id
        self.game_version = game_version
        self.hash = hash
        self.instance = instance
        self.project_id = project_id
        self.resolution = resolution
        self.version_name = version_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.download_type is not None:
            result['DownloadType'] = self.download_type
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.game_version is not None:
            result['GameVersion'] = self.game_version
        if self.hash is not None:
            result['Hash'] = self.hash
        if self.instance is not None:
            result['Instance'] = self.instance
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadType') is not None:
            self.download_type = m.get('DownloadType')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('GameVersion') is not None:
            self.game_version = m.get('GameVersion')
        if m.get('Hash') is not None:
            self.hash = m.get('Hash')
        if m.get('Instance') is not None:
            self.instance = m.get('Instance')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class CreateGameDeployWorkflowResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 任务id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateGameDeployWorkflowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateGameDeployWorkflowResponseBody = None,
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
            temp_model = CreateGameDeployWorkflowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOrderRequest(TeaModel):
    def __init__(
        self,
        account_domain: str = None,
        amount: int = None,
        buyer_account_id: str = None,
        idempotent_code: str = None,
        item_id: str = None,
        origin_price: int = None,
        settlement_price: int = None,
        sku_id: str = None,
    ):
        self.account_domain = account_domain
        self.amount = amount
        self.buyer_account_id = buyer_account_id
        self.idempotent_code = idempotent_code
        self.item_id = item_id
        self.origin_price = origin_price
        self.settlement_price = settlement_price
        self.sku_id = sku_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_domain is not None:
            result['AccountDomain'] = self.account_domain
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.buyer_account_id is not None:
            result['BuyerAccountId'] = self.buyer_account_id
        if self.idempotent_code is not None:
            result['IdempotentCode'] = self.idempotent_code
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.origin_price is not None:
            result['OriginPrice'] = self.origin_price
        if self.settlement_price is not None:
            result['SettlementPrice'] = self.settlement_price
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountDomain') is not None:
            self.account_domain = m.get('AccountDomain')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('BuyerAccountId') is not None:
            self.buyer_account_id = m.get('BuyerAccountId')
        if m.get('IdempotentCode') is not None:
            self.idempotent_code = m.get('IdempotentCode')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('OriginPrice') is not None:
            self.origin_price = m.get('OriginPrice')
        if m.get('SettlementPrice') is not None:
            self.settlement_price = m.get('SettlementPrice')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        return self


class CreateOrderResponseBodyData(TeaModel):
    def __init__(
        self,
        account_domain: str = None,
        amount: int = None,
        apply_delivery_time: int = None,
        auto_unlock_time: int = None,
        buyer_account_id: str = None,
        create_time: int = None,
        finish_time: int = None,
        item_id: str = None,
        order_id: str = None,
        origin_price: int = None,
        settlement_price: int = None,
        sku_id: str = None,
        status: str = None,
    ):
        self.account_domain = account_domain
        self.amount = amount
        self.apply_delivery_time = apply_delivery_time
        self.auto_unlock_time = auto_unlock_time
        self.buyer_account_id = buyer_account_id
        self.create_time = create_time
        self.finish_time = finish_time
        self.item_id = item_id
        self.order_id = order_id
        self.origin_price = origin_price
        self.settlement_price = settlement_price
        self.sku_id = sku_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_domain is not None:
            result['AccountDomain'] = self.account_domain
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.apply_delivery_time is not None:
            result['ApplyDeliveryTime'] = self.apply_delivery_time
        if self.auto_unlock_time is not None:
            result['AutoUnlockTime'] = self.auto_unlock_time
        if self.buyer_account_id is not None:
            result['BuyerAccountId'] = self.buyer_account_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.origin_price is not None:
            result['OriginPrice'] = self.origin_price
        if self.settlement_price is not None:
            result['SettlementPrice'] = self.settlement_price
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountDomain') is not None:
            self.account_domain = m.get('AccountDomain')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('ApplyDeliveryTime') is not None:
            self.apply_delivery_time = m.get('ApplyDeliveryTime')
        if m.get('AutoUnlockTime') is not None:
            self.auto_unlock_time = m.get('AutoUnlockTime')
        if m.get('BuyerAccountId') is not None:
            self.buyer_account_id = m.get('BuyerAccountId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OriginPrice') is not None:
            self.origin_price = m.get('OriginPrice')
        if m.get('SettlementPrice') is not None:
            self.settlement_price = m.get('SettlementPrice')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateOrderResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateOrderResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateOrderResponseBody = None,
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
            temp_model = CreateOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProjectRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        project_name: str = None,
    ):
        # 幂等参数，1-64位建议使用uuid
        self.client_token = client_token
        # 项目名称
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class CreateProjectResponseBody(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        request_id: str = None,
    ):
        # 项目ID
        self.project_id = project_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateProjectResponseBody = None,
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
            temp_model = CreateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTokenRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        current_token: str = None,
        session: str = None,
    ):
        self.client_token = client_token
        self.current_token = current_token
        self.session = session

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.current_token is not None:
            result['CurrentToken'] = self.current_token
        if self.session is not None:
            result['Session'] = self.session
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CurrentToken') is not None:
            self.current_token = m.get('CurrentToken')
        if m.get('Session') is not None:
            self.session = m.get('Session')
        return self


class CreateTokenResponseBodyData(TeaModel):
    def __init__(
        self,
        token: str = None,
    ):
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class CreateTokenResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateTokenResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateTokenResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateTokenResponseBody = None,
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
            temp_model = CreateTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGameRequest(TeaModel):
    def __init__(
        self,
        game_id: str = None,
    ):
        # 游戏ID
        self.game_id = game_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.game_id is not None:
            result['GameId'] = self.game_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        return self


class DeleteGameResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteGameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteGameResponseBody = None,
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
            temp_model = DeleteGameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGameVersionRequest(TeaModel):
    def __init__(
        self,
        version_id: str = None,
    ):
        # 游戏版本ID
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class DeleteGameVersionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteGameVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteGameVersionResponseBody = None,
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
            temp_model = DeleteGameVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProjectRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
    ):
        # 项目ID
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DeleteProjectResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteProjectResponseBody = None,
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
            temp_model = DeleteProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeliveryOrderRequest(TeaModel):
    def __init__(
        self,
        account_domain: str = None,
        buyer_account_id: str = None,
        order_id: str = None,
    ):
        self.account_domain = account_domain
        self.buyer_account_id = buyer_account_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_domain is not None:
            result['AccountDomain'] = self.account_domain
        if self.buyer_account_id is not None:
            result['BuyerAccountId'] = self.buyer_account_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountDomain') is not None:
            self.account_domain = m.get('AccountDomain')
        if m.get('BuyerAccountId') is not None:
            self.buyer_account_id = m.get('BuyerAccountId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class DeliveryOrderResponseBodyData(TeaModel):
    def __init__(
        self,
        delivery_status: str = None,
    ):
        self.delivery_status = delivery_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_status is not None:
            result['DeliveryStatus'] = self.delivery_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryStatus') is not None:
            self.delivery_status = m.get('DeliveryStatus')
        return self


class DeliveryOrderResponseBody(TeaModel):
    def __init__(
        self,
        data: DeliveryOrderResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DeliveryOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeliveryOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeliveryOrderResponseBody = None,
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
            temp_model = DeliveryOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DispatchGameSlotRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        biz_param: str = None,
        cancel: bool = None,
        client_ip: str = None,
        game_command: str = None,
        game_id: str = None,
        game_session: str = None,
        game_start_param: str = None,
        reconnect: bool = None,
        region_name: str = None,
        system_info: str = None,
        tags: str = None,
        user_id: str = None,
        user_level: int = None,
    ):
        self.access_key = access_key
        self.biz_param = biz_param
        self.cancel = cancel
        self.client_ip = client_ip
        self.game_command = game_command
        self.game_id = game_id
        self.game_session = game_session
        self.game_start_param = game_start_param
        self.reconnect = reconnect
        self.region_name = region_name
        self.system_info = system_info
        self.tags = tags
        self.user_id = user_id
        self.user_level = user_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.biz_param is not None:
            result['BizParam'] = self.biz_param
        if self.cancel is not None:
            result['Cancel'] = self.cancel
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.game_command is not None:
            result['GameCommand'] = self.game_command
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.game_session is not None:
            result['GameSession'] = self.game_session
        if self.game_start_param is not None:
            result['GameStartParam'] = self.game_start_param
        if self.reconnect is not None:
            result['Reconnect'] = self.reconnect
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.system_info is not None:
            result['SystemInfo'] = self.system_info
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_level is not None:
            result['UserLevel'] = self.user_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('BizParam') is not None:
            self.biz_param = m.get('BizParam')
        if m.get('Cancel') is not None:
            self.cancel = m.get('Cancel')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('GameCommand') is not None:
            self.game_command = m.get('GameCommand')
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('GameSession') is not None:
            self.game_session = m.get('GameSession')
        if m.get('GameStartParam') is not None:
            self.game_start_param = m.get('GameStartParam')
        if m.get('Reconnect') is not None:
            self.reconnect = m.get('Reconnect')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('SystemInfo') is not None:
            self.system_info = m.get('SystemInfo')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserLevel') is not None:
            self.user_level = m.get('UserLevel')
        return self


class DispatchGameSlotResponseBody(TeaModel):
    def __init__(
        self,
        game_id: str = None,
        game_session: str = None,
        message: str = None,
        queue_code: int = None,
        queue_state: int = None,
        region_name: str = None,
        request_id: str = None,
        user_id: str = None,
    ):
        self.game_id = game_id
        self.game_session = game_session
        self.message = message
        self.queue_code = queue_code
        self.queue_state = queue_state
        self.region_name = region_name
        self.request_id = request_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.game_session is not None:
            result['GameSession'] = self.game_session
        if self.message is not None:
            result['Message'] = self.message
        if self.queue_code is not None:
            result['QueueCode'] = self.queue_code
        if self.queue_state is not None:
            result['QueueState'] = self.queue_state
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('GameSession') is not None:
            self.game_session = m.get('GameSession')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('QueueCode') is not None:
            self.queue_code = m.get('QueueCode')
        if m.get('QueueState') is not None:
            self.queue_state = m.get('QueueState')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DispatchGameSlotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DispatchGameSlotResponseBody = None,
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
            temp_model = DispatchGameSlotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGameCcuRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        game_id: str = None,
        region_name: str = None,
    ):
        self.access_key = access_key
        self.game_id = game_id
        self.region_name = region_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        return self


class GetGameCcuResponseBodyDataList(TeaModel):
    def __init__(
        self,
        ccu: int = None,
        game_id: str = None,
        region_id: str = None,
    ):
        self.ccu = ccu
        self.game_id = game_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ccu is not None:
            result['Ccu'] = self.ccu
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ccu') is not None:
            self.ccu = m.get('Ccu')
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetGameCcuResponseBody(TeaModel):
    def __init__(
        self,
        data_list: List[GetGameCcuResponseBodyDataList] = None,
        request_id: str = None,
    ):
        self.data_list = data_list
        self.request_id = request_id

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = GetGameCcuResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetGameCcuResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetGameCcuResponseBody = None,
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
            temp_model = GetGameCcuResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGameStatusRequest(TeaModel):
    def __init__(
        self,
        game_session: str = None,
    ):
        self.game_session = game_session

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.game_session is not None:
            result['GameSession'] = self.game_session
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GameSession') is not None:
            self.game_session = m.get('GameSession')
        return self


class GetGameStatusResponseBodyDataPlayingUsers(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        start_play_time: int = None,
    ):
        self.account_id = account_id
        self.start_play_time = start_play_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.start_play_time is not None:
            result['StartPlayTime'] = self.start_play_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('StartPlayTime') is not None:
            self.start_play_time = m.get('StartPlayTime')
        return self


class GetGameStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        game_id: str = None,
        game_session: str = None,
        game_start_at: int = None,
        playing_count: int = None,
        playing_users: List[GetGameStatusResponseBodyDataPlayingUsers] = None,
    ):
        self.game_id = game_id
        self.game_session = game_session
        self.game_start_at = game_start_at
        self.playing_count = playing_count
        self.playing_users = playing_users

    def validate(self):
        if self.playing_users:
            for k in self.playing_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.game_session is not None:
            result['GameSession'] = self.game_session
        if self.game_start_at is not None:
            result['GameStartAt'] = self.game_start_at
        if self.playing_count is not None:
            result['PlayingCount'] = self.playing_count
        result['PlayingUsers'] = []
        if self.playing_users is not None:
            for k in self.playing_users:
                result['PlayingUsers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('GameSession') is not None:
            self.game_session = m.get('GameSession')
        if m.get('GameStartAt') is not None:
            self.game_start_at = m.get('GameStartAt')
        if m.get('PlayingCount') is not None:
            self.playing_count = m.get('PlayingCount')
        self.playing_users = []
        if m.get('PlayingUsers') is not None:
            for k in m.get('PlayingUsers'):
                temp_model = GetGameStatusResponseBodyDataPlayingUsers()
                self.playing_users.append(temp_model.from_map(k))
        return self


class GetGameStatusResponseBody(TeaModel):
    def __init__(
        self,
        data: GetGameStatusResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetGameStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetGameStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetGameStatusResponseBody = None,
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
            temp_model = GetGameStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGameStockRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        game_id: str = None,
        user_level: int = None,
    ):
        self.access_key = access_key
        self.game_id = game_id
        self.user_level = user_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.user_level is not None:
            result['UserLevel'] = self.user_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('UserLevel') is not None:
            self.user_level = m.get('UserLevel')
        return self


class GetGameStockResponseBodyInstanceStockList(TeaModel):
    def __init__(
        self,
        available_slots: int = None,
        instance_id: str = None,
        instance_spec: str = None,
        regin_name: str = None,
        user_level: int = None,
    ):
        self.available_slots = available_slots
        self.instance_id = instance_id
        self.instance_spec = instance_spec
        self.regin_name = regin_name
        self.user_level = user_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_slots is not None:
            result['AvailableSlots'] = self.available_slots
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec
        if self.regin_name is not None:
            result['ReginName'] = self.regin_name
        if self.user_level is not None:
            result['UserLevel'] = self.user_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableSlots') is not None:
            self.available_slots = m.get('AvailableSlots')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')
        if m.get('ReginName') is not None:
            self.regin_name = m.get('ReginName')
        if m.get('UserLevel') is not None:
            self.user_level = m.get('UserLevel')
        return self


class GetGameStockResponseBody(TeaModel):
    def __init__(
        self,
        game_id: str = None,
        instance_stock_list: List[GetGameStockResponseBodyInstanceStockList] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.game_id = game_id
        self.instance_stock_list = instance_stock_list
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.instance_stock_list:
            for k in self.instance_stock_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.game_id is not None:
            result['GameId'] = self.game_id
        result['InstanceStockList'] = []
        if self.instance_stock_list is not None:
            for k in self.instance_stock_list:
                result['InstanceStockList'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        self.instance_stock_list = []
        if m.get('InstanceStockList') is not None:
            for k in m.get('InstanceStockList'):
                temp_model = GetGameStockResponseBodyInstanceStockList()
                self.instance_stock_list.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetGameStockResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetGameStockResponseBody = None,
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
            temp_model = GetGameStockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGameTrialSurplusDurationRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        game_id: str = None,
        project_id: str = None,
    ):
        # 账号ID
        self.account_id = account_id
        # 游戏ID
        self.game_id = game_id
        # 项目ID
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class GetGameTrialSurplusDurationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        status: float = None,
        surplus_duration: float = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 状态
        self.status = status
        # 剩余试玩时长
        self.surplus_duration = surplus_duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.surplus_duration is not None:
            result['SurplusDuration'] = self.surplus_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SurplusDuration') is not None:
            self.surplus_duration = m.get('SurplusDuration')
        return self


class GetGameTrialSurplusDurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetGameTrialSurplusDurationResponseBody = None,
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
            temp_model = GetGameTrialSurplusDurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGameVersionRequest(TeaModel):
    def __init__(
        self,
        version_id: str = None,
    ):
        # 版本ID
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class GetGameVersionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        version_id: str = None,
        version_name: str = None,
        version_number: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 版本ID
        self.version_id = version_id
        # 版本名称
        self.version_name = version_name
        # 版本号
        self.version_number = version_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        if self.version_number is not None:
            result['VersionNumber'] = self.version_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        if m.get('VersionNumber') is not None:
            self.version_number = m.get('VersionNumber')
        return self


class GetGameVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetGameVersionResponseBody = None,
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
            temp_model = GetGameVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGameVersionProgressRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # 任务id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetGameVersionProgressResponseBody(TeaModel):
    def __init__(
        self,
        description: str = None,
        event: str = None,
        extra: Dict[str, Any] = None,
        request_id: str = None,
        status: str = None,
    ):
        self.description = description
        self.event = event
        self.extra = extra
        # Id of the request
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.event is not None:
            result['Event'] = self.event
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetGameVersionProgressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetGameVersionProgressResponseBody = None,
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
            temp_model = GetGameVersionProgressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetItemRequest(TeaModel):
    def __init__(
        self,
        item_id: str = None,
    ):
        self.item_id = item_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        return self


class GetItemResponseBodyDataGames(TeaModel):
    def __init__(
        self,
        game_id: str = None,
        name: str = None,
    ):
        self.game_id = game_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetItemResponseBodyDataSkusSaleProps(TeaModel):
    def __init__(
        self,
        property_id: int = None,
        property_name: str = None,
        value: str = None,
        value_id: int = None,
    ):
        self.property_id = property_id
        self.property_name = property_name
        self.value = value
        self.value_id = value_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_id is not None:
            result['PropertyId'] = self.property_id
        if self.property_name is not None:
            result['PropertyName'] = self.property_name
        if self.value is not None:
            result['Value'] = self.value
        if self.value_id is not None:
            result['ValueId'] = self.value_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')
        if m.get('PropertyName') is not None:
            self.property_name = m.get('PropertyName')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('ValueId') is not None:
            self.value_id = m.get('ValueId')
        return self


class GetItemResponseBodyDataSkus(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        item_id: str = None,
        modify_time: int = None,
        origin_price: int = None,
        sale_price: int = None,
        sale_props: List[GetItemResponseBodyDataSkusSaleProps] = None,
        sku_id: str = None,
        status: int = None,
    ):
        self.create_time = create_time
        self.item_id = item_id
        self.modify_time = modify_time
        self.origin_price = origin_price
        self.sale_price = sale_price
        self.sale_props = sale_props
        self.sku_id = sku_id
        self.status = status

    def validate(self):
        if self.sale_props:
            for k in self.sale_props:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.origin_price is not None:
            result['OriginPrice'] = self.origin_price
        if self.sale_price is not None:
            result['SalePrice'] = self.sale_price
        result['SaleProps'] = []
        if self.sale_props is not None:
            for k in self.sale_props:
                result['SaleProps'].append(k.to_map() if k else None)
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('OriginPrice') is not None:
            self.origin_price = m.get('OriginPrice')
        if m.get('SalePrice') is not None:
            self.sale_price = m.get('SalePrice')
        self.sale_props = []
        if m.get('SaleProps') is not None:
            for k in m.get('SaleProps'):
                temp_model = GetItemResponseBodyDataSkusSaleProps()
                self.sale_props.append(temp_model.from_map(k))
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetItemResponseBodyData(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        create_time: int = None,
        description: str = None,
        games: List[GetItemResponseBodyDataGames] = None,
        item_id: str = None,
        modify_time: int = None,
        origin_price: int = None,
        sale_price: int = None,
        seller_id: str = None,
        skus: List[GetItemResponseBodyDataSkus] = None,
        status: int = None,
        supplier: str = None,
        title: str = None,
    ):
        self.category_id = category_id
        self.create_time = create_time
        self.description = description
        self.games = games
        self.item_id = item_id
        self.modify_time = modify_time
        self.origin_price = origin_price
        self.sale_price = sale_price
        self.seller_id = seller_id
        self.skus = skus
        self.status = status
        self.supplier = supplier
        self.title = title

    def validate(self):
        if self.games:
            for k in self.games:
                if k:
                    k.validate()
        if self.skus:
            for k in self.skus:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        result['Games'] = []
        if self.games is not None:
            for k in self.games:
                result['Games'].append(k.to_map() if k else None)
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.origin_price is not None:
            result['OriginPrice'] = self.origin_price
        if self.sale_price is not None:
            result['SalePrice'] = self.sale_price
        if self.seller_id is not None:
            result['SellerId'] = self.seller_id
        result['Skus'] = []
        if self.skus is not None:
            for k in self.skus:
                result['Skus'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        if self.supplier is not None:
            result['Supplier'] = self.supplier
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.games = []
        if m.get('Games') is not None:
            for k in m.get('Games'):
                temp_model = GetItemResponseBodyDataGames()
                self.games.append(temp_model.from_map(k))
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('OriginPrice') is not None:
            self.origin_price = m.get('OriginPrice')
        if m.get('SalePrice') is not None:
            self.sale_price = m.get('SalePrice')
        if m.get('SellerId') is not None:
            self.seller_id = m.get('SellerId')
        self.skus = []
        if m.get('Skus') is not None:
            for k in m.get('Skus'):
                temp_model = GetItemResponseBodyDataSkus()
                self.skus.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Supplier') is not None:
            self.supplier = m.get('Supplier')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetItemResponseBody(TeaModel):
    def __init__(
        self,
        data: GetItemResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetItemResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetItemResponseBody = None,
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
            temp_model = GetItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOutAccountBindDetailRequest(TeaModel):
    def __init__(
        self,
        account_domain: str = None,
        account_id: str = None,
        out_account_type: str = None,
    ):
        self.account_domain = account_domain
        self.account_id = account_id
        self.out_account_type = out_account_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_domain is not None:
            result['AccountDomain'] = self.account_domain
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.out_account_type is not None:
            result['OutAccountType'] = self.out_account_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountDomain') is not None:
            self.account_domain = m.get('AccountDomain')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('OutAccountType') is not None:
            self.out_account_type = m.get('OutAccountType')
        return self


class GetOutAccountBindDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        bind_status: int = None,
        out_account_id: str = None,
        out_account_type: str = None,
        token: str = None,
        token_expire_time: int = None,
    ):
        self.bind_status = bind_status
        self.out_account_id = out_account_id
        self.out_account_type = out_account_type
        self.token = token
        self.token_expire_time = token_expire_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_status is not None:
            result['BindStatus'] = self.bind_status
        if self.out_account_id is not None:
            result['OutAccountId'] = self.out_account_id
        if self.out_account_type is not None:
            result['OutAccountType'] = self.out_account_type
        if self.token is not None:
            result['Token'] = self.token
        if self.token_expire_time is not None:
            result['TokenExpireTime'] = self.token_expire_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindStatus') is not None:
            self.bind_status = m.get('BindStatus')
        if m.get('OutAccountId') is not None:
            self.out_account_id = m.get('OutAccountId')
        if m.get('OutAccountType') is not None:
            self.out_account_type = m.get('OutAccountType')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('TokenExpireTime') is not None:
            self.token_expire_time = m.get('TokenExpireTime')
        return self


class GetOutAccountBindDetailResponseBody(TeaModel):
    def __init__(
        self,
        data: GetOutAccountBindDetailResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetOutAccountBindDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetOutAccountBindDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetOutAccountBindDetailResponseBody = None,
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
            temp_model = GetOutAccountBindDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSessionRequest(TeaModel):
    def __init__(
        self,
        token: str = None,
    ):
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class GetSessionResponseBodyData(TeaModel):
    def __init__(
        self,
        session: str = None,
    ):
        self.session = session

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session is not None:
            result['Session'] = self.session
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Session') is not None:
            self.session = m.get('Session')
        return self


class GetSessionResponseBody(TeaModel):
    def __init__(
        self,
        data: GetSessionResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetSessionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSessionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSessionResponseBody = None,
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
            temp_model = GetSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStopGameTokenRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        game_id: str = None,
    ):
        self.access_key = access_key
        self.game_id = game_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.game_id is not None:
            result['GameId'] = self.game_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        return self


class GetStopGameTokenResponseBody(TeaModel):
    def __init__(
        self,
        expire_time: int = None,
        request_id: str = None,
        token: str = None,
    ):
        self.expire_time = expire_time
        self.request_id = request_id
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class GetStopGameTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetStopGameTokenResponseBody = None,
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
            temp_model = GetStopGameTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class KickPlayerRequest(TeaModel):
    def __init__(
        self,
        game_session: str = None,
        kicked_account_id: str = None,
    ):
        self.game_session = game_session
        self.kicked_account_id = kicked_account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.game_session is not None:
            result['GameSession'] = self.game_session
        if self.kicked_account_id is not None:
            result['KickedAccountId'] = self.kicked_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GameSession') is not None:
            self.game_session = m.get('GameSession')
        if m.get('KickedAccountId') is not None:
            self.kicked_account_id = m.get('KickedAccountId')
        return self


class KickPlayerResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class KickPlayerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: KickPlayerResponseBody = None,
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
            temp_model = KickPlayerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBoughtGamesRequest(TeaModel):
    def __init__(
        self,
        account_domain: str = None,
        account_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.account_domain = account_domain
        self.account_id = account_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_domain is not None:
            result['AccountDomain'] = self.account_domain
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountDomain') is not None:
            self.account_domain = m.get('AccountDomain')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListBoughtGamesResponseBodyItems(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        game_id: str = None,
        game_name: str = None,
        start_time: int = None,
    ):
        self.end_time = end_time
        self.game_id = game_id
        self.game_name = game_name
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.game_name is not None:
            result['GameName'] = self.game_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('GameName') is not None:
            self.game_name = m.get('GameName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListBoughtGamesResponseBody(TeaModel):
    def __init__(
        self,
        items: List[ListBoughtGamesResponseBodyItems] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListBoughtGamesResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListBoughtGamesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListBoughtGamesResponseBody = None,
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
            temp_model = ListBoughtGamesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListContainerStatusRequestGameSessionIdList(TeaModel):
    def __init__(
        self,
        game_session_id: str = None,
    ):
        self.game_session_id = game_session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.game_session_id is not None:
            result['GameSessionId'] = self.game_session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GameSessionId') is not None:
            self.game_session_id = m.get('GameSessionId')
        return self


class ListContainerStatusRequest(TeaModel):
    def __init__(
        self,
        game_session_id_list: List[ListContainerStatusRequestGameSessionIdList] = None,
    ):
        self.game_session_id_list = game_session_id_list

    def validate(self):
        if self.game_session_id_list:
            for k in self.game_session_id_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['GameSessionIdList'] = []
        if self.game_session_id_list is not None:
            for k in self.game_session_id_list:
                result['GameSessionIdList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.game_session_id_list = []
        if m.get('GameSessionIdList') is not None:
            for k in m.get('GameSessionIdList'):
                temp_model = ListContainerStatusRequestGameSessionIdList()
                self.game_session_id_list.append(temp_model.from_map(k))
        return self


class ListContainerStatusResponseBodyDataListPlayerDetailList(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        is_initiator: bool = None,
        start_time: int = None,
    ):
        self.account_id = account_id
        self.is_initiator = is_initiator
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.is_initiator is not None:
            result['IsInitiator'] = self.is_initiator
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('IsInitiator') is not None:
            self.is_initiator = m.get('IsInitiator')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListContainerStatusResponseBodyDataList(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        container_quit_time: int = None,
        container_start_time: int = None,
        container_state: str = None,
        game_id: str = None,
        game_session_id: str = None,
        player_detail_list: List[ListContainerStatusResponseBodyDataListPlayerDetailList] = None,
        project_id: str = None,
        tags: str = None,
        timestamp: int = None,
    ):
        self.account_id = account_id
        self.container_quit_time = container_quit_time
        self.container_start_time = container_start_time
        self.container_state = container_state
        self.game_id = game_id
        self.game_session_id = game_session_id
        self.player_detail_list = player_detail_list
        self.project_id = project_id
        self.tags = tags
        # 系统时间戳
        self.timestamp = timestamp

    def validate(self):
        if self.player_detail_list:
            for k in self.player_detail_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.container_quit_time is not None:
            result['ContainerQuitTime'] = self.container_quit_time
        if self.container_start_time is not None:
            result['ContainerStartTime'] = self.container_start_time
        if self.container_state is not None:
            result['ContainerState'] = self.container_state
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.game_session_id is not None:
            result['GameSessionId'] = self.game_session_id
        result['PlayerDetailList'] = []
        if self.player_detail_list is not None:
            for k in self.player_detail_list:
                result['PlayerDetailList'].append(k.to_map() if k else None)
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ContainerQuitTime') is not None:
            self.container_quit_time = m.get('ContainerQuitTime')
        if m.get('ContainerStartTime') is not None:
            self.container_start_time = m.get('ContainerStartTime')
        if m.get('ContainerState') is not None:
            self.container_state = m.get('ContainerState')
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('GameSessionId') is not None:
            self.game_session_id = m.get('GameSessionId')
        self.player_detail_list = []
        if m.get('PlayerDetailList') is not None:
            for k in m.get('PlayerDetailList'):
                temp_model = ListContainerStatusResponseBodyDataListPlayerDetailList()
                self.player_detail_list.append(temp_model.from_map(k))
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class ListContainerStatusResponseBody(TeaModel):
    def __init__(
        self,
        data_list: List[ListContainerStatusResponseBodyDataList] = None,
        request_id: str = None,
    ):
        self.data_list = data_list
        self.request_id = request_id

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = ListContainerStatusResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListContainerStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListContainerStatusResponseBody = None,
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
            temp_model = ListContainerStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeployableInstancesRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        version_id: str = None,
    ):
        # 页码
        self.page_number = page_number
        # 每页大小
        self.page_size = page_size
        # 项目ID
        self.project_id = project_id
        # 游戏版本ID
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class ListDeployableInstancesResponseBodyDataList(TeaModel):
    def __init__(
        self,
        cloud_game_instance_id: str = None,
        cloud_game_instance_name: str = None,
    ):
        # 实例ID
        self.cloud_game_instance_id = cloud_game_instance_id
        # 实例名称
        self.cloud_game_instance_name = cloud_game_instance_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_game_instance_id is not None:
            result['CloudGameInstanceId'] = self.cloud_game_instance_id
        if self.cloud_game_instance_name is not None:
            result['CloudGameInstanceName'] = self.cloud_game_instance_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudGameInstanceId') is not None:
            self.cloud_game_instance_id = m.get('CloudGameInstanceId')
        if m.get('CloudGameInstanceName') is not None:
            self.cloud_game_instance_name = m.get('CloudGameInstanceName')
        return self


class ListDeployableInstancesResponseBody(TeaModel):
    def __init__(
        self,
        data_list: List[ListDeployableInstancesResponseBodyDataList] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # 数据列表
        self.data_list = data_list
        # 表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.page_number = page_number
        # MaxResults本次请求所返回的最大记录条数
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        # TotalCount本次请求条件下的数据总量，此参数为可选参数，默认可不返回
        self.total_count = total_count

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = ListDeployableInstancesResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDeployableInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDeployableInstancesResponseBody = None,
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
            temp_model = ListDeployableInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGameVersionsRequest(TeaModel):
    def __init__(
        self,
        game_id: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # 游戏ID
        self.game_id = game_id
        # 本次读取的最大数据记录数量
        self.max_results = max_results
        # 标记当前开始读取的位置，置空表示从头开始
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListGameVersionsResponseBodyDataList(TeaModel):
    def __init__(
        self,
        version_id: str = None,
        version_name: str = None,
        version_number: str = None,
    ):
        # 版本ID
        self.version_id = version_id
        # 版本名称
        self.version_name = version_name
        # 版本号
        self.version_number = version_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        if self.version_number is not None:
            result['VersionNumber'] = self.version_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        if m.get('VersionNumber') is not None:
            self.version_number = m.get('VersionNumber')
        return self


class ListGameVersionsResponseBody(TeaModel):
    def __init__(
        self,
        count: int = None,
        data_list: List[ListGameVersionsResponseBodyDataList] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # 总记录数
        self.count = count
        # 数据列表
        self.data_list = data_list
        # 本次请求所返回的最大记录条数
        self.max_results = max_results
        # 表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = ListGameVersionsResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListGameVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListGameVersionsResponseBody = None,
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
            temp_model = ListGameVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGamesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
    ):
        # 本次读取的最大数据记录数量
        self.max_results = max_results
        # 标记当前开始读取的位置，置空表示从头开始
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListGamesResponseBodyDataList(TeaModel):
    def __init__(
        self,
        game_id: str = None,
        game_name: str = None,
        platform_type: int = None,
    ):
        # 游戏ID
        self.game_id = game_id
        # 游戏名称
        self.game_name = game_name
        # 平台类型
        self.platform_type = platform_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.game_name is not None:
            result['GameName'] = self.game_name
        if self.platform_type is not None:
            result['PlatformType'] = self.platform_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('GameName') is not None:
            self.game_name = m.get('GameName')
        if m.get('PlatformType') is not None:
            self.platform_type = m.get('PlatformType')
        return self


class ListGamesResponseBody(TeaModel):
    def __init__(
        self,
        count: int = None,
        data_list: List[ListGamesResponseBodyDataList] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # 总记录数
        self.count = count
        # 数据列表
        self.data_list = data_list
        # 本次请求所返回的最大记录条数
        self.max_results = max_results
        # 表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = ListGamesResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListGamesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListGamesResponseBody = None,
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
            temp_model = ListGamesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHistoryContainerStatusRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        last_game_session_id: str = None,
        page_size: int = None,
        project_id: str = None,
        start_time: int = None,
    ):
        # 结束时间（Linux时间戳，单位毫秒）
        self.end_time = end_time
        # 上一个游戏会话ID
        self.last_game_session_id = last_game_session_id
        # 每页数量
        self.page_size = page_size
        # 项目ID
        self.project_id = project_id
        # 开始时间（Linux时间戳，单位毫秒）
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.last_game_session_id is not None:
            result['LastGameSessionId'] = self.last_game_session_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('LastGameSessionId') is not None:
            self.last_game_session_id = m.get('LastGameSessionId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListHistoryContainerStatusResponseBodyDataListPlayerDetailList(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        is_initiator: bool = None,
        start_time: int = None,
    ):
        # 账号ID
        self.account_id = account_id
        # 是否主机
        self.is_initiator = is_initiator
        # 玩家进入游戏时间
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.is_initiator is not None:
            result['IsInitiator'] = self.is_initiator
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('IsInitiator') is not None:
            self.is_initiator = m.get('IsInitiator')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListHistoryContainerStatusResponseBodyDataList(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        container_quit_time: int = None,
        container_start_time: int = None,
        container_state: str = None,
        game_id: str = None,
        game_session_id: str = None,
        player_detail_list: List[ListHistoryContainerStatusResponseBodyDataListPlayerDetailList] = None,
        project_id: str = None,
        tags: str = None,
        timestamp: int = None,
    ):
        # 主机账号ID
        self.account_id = account_id
        # 容器退出时间（Linux时间戳，单位毫秒）
        self.container_quit_time = container_quit_time
        # 容器启动时间（Linux时间戳，单位毫秒）
        self.container_start_time = container_start_time
        # 容器状态
        self.container_state = container_state
        # 游戏ID
        self.game_id = game_id
        # 游戏会话ID
        self.game_session_id = game_session_id
        # 玩家信息集合
        self.player_detail_list = player_detail_list
        # 项目ID
        self.project_id = project_id
        # 自定义标识
        self.tags = tags
        # 系统时间戳
        self.timestamp = timestamp

    def validate(self):
        if self.player_detail_list:
            for k in self.player_detail_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.container_quit_time is not None:
            result['ContainerQuitTime'] = self.container_quit_time
        if self.container_start_time is not None:
            result['ContainerStartTime'] = self.container_start_time
        if self.container_state is not None:
            result['ContainerState'] = self.container_state
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.game_session_id is not None:
            result['GameSessionId'] = self.game_session_id
        result['PlayerDetailList'] = []
        if self.player_detail_list is not None:
            for k in self.player_detail_list:
                result['PlayerDetailList'].append(k.to_map() if k else None)
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ContainerQuitTime') is not None:
            self.container_quit_time = m.get('ContainerQuitTime')
        if m.get('ContainerStartTime') is not None:
            self.container_start_time = m.get('ContainerStartTime')
        if m.get('ContainerState') is not None:
            self.container_state = m.get('ContainerState')
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('GameSessionId') is not None:
            self.game_session_id = m.get('GameSessionId')
        self.player_detail_list = []
        if m.get('PlayerDetailList') is not None:
            for k in m.get('PlayerDetailList'):
                temp_model = ListHistoryContainerStatusResponseBodyDataListPlayerDetailList()
                self.player_detail_list.append(temp_model.from_map(k))
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class ListHistoryContainerStatusResponseBody(TeaModel):
    def __init__(
        self,
        data_list: List[ListHistoryContainerStatusResponseBodyDataList] = None,
        request_id: str = None,
    ):
        # 容器状态信息集合
        self.data_list = data_list
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = ListHistoryContainerStatusResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListHistoryContainerStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListHistoryContainerStatusResponseBody = None,
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
            temp_model = ListHistoryContainerStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
    ):
        # 本次读取的最大数据记录数量
        self.max_results = max_results
        # 标记当前开始读取的位置，置空表示从头开始
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListProjectsResponseBodyDataList(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        project_name: str = None,
    ):
        # 项目ID
        self.project_id = project_id
        # 项目名称
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class ListProjectsResponseBody(TeaModel):
    def __init__(
        self,
        count: int = None,
        data_list: List[ListProjectsResponseBodyDataList] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # 总记录数
        self.count = count
        # 数据列表
        self.data_list = data_list
        # 本次请求所返回的最大记录条数
        self.max_results = max_results
        # 表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = ListProjectsResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListProjectsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListProjectsResponseBody = None,
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
            temp_model = ListProjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryGameRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        project_id: int = None,
        tenant_id: int = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.project_id = project_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryGameResponseBodyData(TeaModel):
    def __init__(
        self,
        game_id: int = None,
        gmt_create: str = None,
        name: str = None,
        project_id: int = None,
        tenant_id: int = None,
        version: str = None,
    ):
        self.game_id = game_id
        self.gmt_create = gmt_create
        self.name = name
        self.project_id = project_id
        self.tenant_id = tenant_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.name is not None:
            result['Name'] = self.name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class QueryGameResponseBody(TeaModel):
    def __init__(
        self,
        data: List[QueryGameResponseBodyData] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.data = data
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryGameResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryGameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryGameResponseBody = None,
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
            temp_model = QueryGameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryItemsRequest(TeaModel):
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
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryItemsResponseBodyDataItemsGames(TeaModel):
    def __init__(
        self,
        game_id: str = None,
        name: str = None,
    ):
        self.game_id = game_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class QueryItemsResponseBodyDataItemsSkusSaleProps(TeaModel):
    def __init__(
        self,
        property_id: int = None,
        property_name: str = None,
        value: str = None,
        value_id: int = None,
    ):
        self.property_id = property_id
        self.property_name = property_name
        self.value = value
        self.value_id = value_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_id is not None:
            result['PropertyId'] = self.property_id
        if self.property_name is not None:
            result['PropertyName'] = self.property_name
        if self.value is not None:
            result['Value'] = self.value
        if self.value_id is not None:
            result['ValueId'] = self.value_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')
        if m.get('PropertyName') is not None:
            self.property_name = m.get('PropertyName')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('ValueId') is not None:
            self.value_id = m.get('ValueId')
        return self


class QueryItemsResponseBodyDataItemsSkus(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        item_id: str = None,
        modify_time: int = None,
        origin_price: int = None,
        sale_price: int = None,
        sale_props: List[QueryItemsResponseBodyDataItemsSkusSaleProps] = None,
        sku_id: str = None,
        status: int = None,
    ):
        self.create_time = create_time
        self.item_id = item_id
        self.modify_time = modify_time
        self.origin_price = origin_price
        self.sale_price = sale_price
        self.sale_props = sale_props
        self.sku_id = sku_id
        self.status = status

    def validate(self):
        if self.sale_props:
            for k in self.sale_props:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.origin_price is not None:
            result['OriginPrice'] = self.origin_price
        if self.sale_price is not None:
            result['SalePrice'] = self.sale_price
        result['SaleProps'] = []
        if self.sale_props is not None:
            for k in self.sale_props:
                result['SaleProps'].append(k.to_map() if k else None)
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('OriginPrice') is not None:
            self.origin_price = m.get('OriginPrice')
        if m.get('SalePrice') is not None:
            self.sale_price = m.get('SalePrice')
        self.sale_props = []
        if m.get('SaleProps') is not None:
            for k in m.get('SaleProps'):
                temp_model = QueryItemsResponseBodyDataItemsSkusSaleProps()
                self.sale_props.append(temp_model.from_map(k))
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryItemsResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        create_time: int = None,
        description: str = None,
        games: List[QueryItemsResponseBodyDataItemsGames] = None,
        item_id: str = None,
        modify_time: int = None,
        origin_price: int = None,
        sale_price: int = None,
        seller_id: str = None,
        skus: List[QueryItemsResponseBodyDataItemsSkus] = None,
        status: int = None,
        supplier: str = None,
        title: str = None,
    ):
        self.category_id = category_id
        self.create_time = create_time
        self.description = description
        self.games = games
        self.item_id = item_id
        self.modify_time = modify_time
        self.origin_price = origin_price
        self.sale_price = sale_price
        self.seller_id = seller_id
        self.skus = skus
        self.status = status
        self.supplier = supplier
        self.title = title

    def validate(self):
        if self.games:
            for k in self.games:
                if k:
                    k.validate()
        if self.skus:
            for k in self.skus:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        result['Games'] = []
        if self.games is not None:
            for k in self.games:
                result['Games'].append(k.to_map() if k else None)
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.origin_price is not None:
            result['OriginPrice'] = self.origin_price
        if self.sale_price is not None:
            result['SalePrice'] = self.sale_price
        if self.seller_id is not None:
            result['SellerId'] = self.seller_id
        result['Skus'] = []
        if self.skus is not None:
            for k in self.skus:
                result['Skus'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        if self.supplier is not None:
            result['Supplier'] = self.supplier
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.games = []
        if m.get('Games') is not None:
            for k in m.get('Games'):
                temp_model = QueryItemsResponseBodyDataItemsGames()
                self.games.append(temp_model.from_map(k))
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('OriginPrice') is not None:
            self.origin_price = m.get('OriginPrice')
        if m.get('SalePrice') is not None:
            self.sale_price = m.get('SalePrice')
        if m.get('SellerId') is not None:
            self.seller_id = m.get('SellerId')
        self.skus = []
        if m.get('Skus') is not None:
            for k in m.get('Skus'):
                temp_model = QueryItemsResponseBodyDataItemsSkus()
                self.skus.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Supplier') is not None:
            self.supplier = m.get('Supplier')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class QueryItemsResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[QueryItemsResponseBodyDataItems] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = QueryItemsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryItemsResponseBody(TeaModel):
    def __init__(
        self,
        data: QueryItemsResponseBodyData = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryItemsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryItemsResponseBody = None,
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
            temp_model = QueryItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOrderRequest(TeaModel):
    def __init__(
        self,
        account_domain: str = None,
        buyer_account_id: str = None,
        order_id: str = None,
    ):
        self.account_domain = account_domain
        self.buyer_account_id = buyer_account_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_domain is not None:
            result['AccountDomain'] = self.account_domain
        if self.buyer_account_id is not None:
            result['BuyerAccountId'] = self.buyer_account_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountDomain') is not None:
            self.account_domain = m.get('AccountDomain')
        if m.get('BuyerAccountId') is not None:
            self.buyer_account_id = m.get('BuyerAccountId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class QueryOrderResponseBodyData(TeaModel):
    def __init__(
        self,
        account_domain: str = None,
        amount: int = None,
        apply_delivery_time: int = None,
        auto_unlock_time: int = None,
        buyer_account_id: str = None,
        create_time: int = None,
        finish_time: int = None,
        item_id: str = None,
        order_id: str = None,
        origin_price: int = None,
        settlement_price: int = None,
        sku_id: str = None,
        status: str = None,
    ):
        self.account_domain = account_domain
        self.amount = amount
        self.apply_delivery_time = apply_delivery_time
        self.auto_unlock_time = auto_unlock_time
        self.buyer_account_id = buyer_account_id
        self.create_time = create_time
        self.finish_time = finish_time
        self.item_id = item_id
        self.order_id = order_id
        self.origin_price = origin_price
        self.settlement_price = settlement_price
        self.sku_id = sku_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_domain is not None:
            result['AccountDomain'] = self.account_domain
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.apply_delivery_time is not None:
            result['ApplyDeliveryTime'] = self.apply_delivery_time
        if self.auto_unlock_time is not None:
            result['AutoUnlockTime'] = self.auto_unlock_time
        if self.buyer_account_id is not None:
            result['BuyerAccountId'] = self.buyer_account_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.origin_price is not None:
            result['OriginPrice'] = self.origin_price
        if self.settlement_price is not None:
            result['SettlementPrice'] = self.settlement_price
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountDomain') is not None:
            self.account_domain = m.get('AccountDomain')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('ApplyDeliveryTime') is not None:
            self.apply_delivery_time = m.get('ApplyDeliveryTime')
        if m.get('AutoUnlockTime') is not None:
            self.auto_unlock_time = m.get('AutoUnlockTime')
        if m.get('BuyerAccountId') is not None:
            self.buyer_account_id = m.get('BuyerAccountId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OriginPrice') is not None:
            self.origin_price = m.get('OriginPrice')
        if m.get('SettlementPrice') is not None:
            self.settlement_price = m.get('SettlementPrice')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryOrderResponseBody(TeaModel):
    def __init__(
        self,
        data: QueryOrderResponseBodyData = None,
        delivery_status: str = None,
        refund_status: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.delivery_status = delivery_status
        self.refund_status = refund_status
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.delivery_status is not None:
            result['DeliveryStatus'] = self.delivery_status
        if self.refund_status is not None:
            result['RefundStatus'] = self.refund_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('DeliveryStatus') is not None:
            self.delivery_status = m.get('DeliveryStatus')
        if m.get('RefundStatus') is not None:
            self.refund_status = m.get('RefundStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryOrderResponseBody = None,
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
            temp_model = QueryOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOutAccountBindStatusRequest(TeaModel):
    def __init__(
        self,
        account_domain: str = None,
        account_id: str = None,
        game_id: str = None,
    ):
        self.account_domain = account_domain
        self.account_id = account_id
        self.game_id = game_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_domain is not None:
            result['AccountDomain'] = self.account_domain
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.game_id is not None:
            result['GameId'] = self.game_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountDomain') is not None:
            self.account_domain = m.get('AccountDomain')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        return self


class QueryOutAccountBindStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        bind_status: int = None,
    ):
        self.bind_status = bind_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_status is not None:
            result['BindStatus'] = self.bind_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindStatus') is not None:
            self.bind_status = m.get('BindStatus')
        return self


class QueryOutAccountBindStatusResponseBody(TeaModel):
    def __init__(
        self,
        data: QueryOutAccountBindStatusResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryOutAccountBindStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryOutAccountBindStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryOutAccountBindStatusResponseBody = None,
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
            temp_model = QueryOutAccountBindStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryProjectRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        project_id: int = None,
        tenant_id: int = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.project_id = project_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryProjectResponseBodyData(TeaModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
        tenant_id: int = None,
    ):
        self.id = id
        self.name = name
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryProjectResponseBody(TeaModel):
    def __init__(
        self,
        data: List[QueryProjectResponseBodyData] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.data = data
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryProjectResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryProjectResponseBody = None,
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
            temp_model = QueryProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTenantRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        param: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.param = param

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.param is not None:
            result['Param'] = self.param
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Param') is not None:
            self.param = m.get('Param')
        return self


class QueryTenantResponseBodyData(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        name: str = None,
        tenant_id: int = None,
    ):
        self.gmt_create = gmt_create
        self.name = name
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.name is not None:
            result['Name'] = self.name
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryTenantResponseBody(TeaModel):
    def __init__(
        self,
        data: List[QueryTenantResponseBodyData] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.data = data
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryTenantResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryTenantResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryTenantResponseBody = None,
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
            temp_model = QueryTenantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveGameFromProjectRequest(TeaModel):
    def __init__(
        self,
        game_id: str = None,
        project_id: str = None,
    ):
        # 游戏iD
        self.game_id = game_id
        # 项目ID
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class RemoveGameFromProjectResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveGameFromProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveGameFromProjectResponseBody = None,
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
            temp_model = RemoveGameFromProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SkipTrialPolicyRequest(TeaModel):
    def __init__(
        self,
        game_session_id: str = None,
    ):
        self.game_session_id = game_session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.game_session_id is not None:
            result['GameSessionId'] = self.game_session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GameSessionId') is not None:
            self.game_session_id = m.get('GameSessionId')
        return self


class SkipTrialPolicyResponseBodyData(TeaModel):
    def __init__(
        self,
        skip_result: int = None,
    ):
        self.skip_result = skip_result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.skip_result is not None:
            result['SkipResult'] = self.skip_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SkipResult') is not None:
            self.skip_result = m.get('SkipResult')
        return self


class SkipTrialPolicyResponseBody(TeaModel):
    def __init__(
        self,
        data: SkipTrialPolicyResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SkipTrialPolicyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SkipTrialPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SkipTrialPolicyResponseBody = None,
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
            temp_model = SkipTrialPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopGameSessionRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        biz_param: str = None,
        game_id: str = None,
        game_session: str = None,
        reason: str = None,
        user_id: str = None,
    ):
        self.access_key = access_key
        self.biz_param = biz_param
        self.game_id = game_id
        self.game_session = game_session
        self.reason = reason
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.biz_param is not None:
            result['BizParam'] = self.biz_param
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.game_session is not None:
            result['GameSession'] = self.game_session
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('BizParam') is not None:
            self.biz_param = m.get('BizParam')
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('GameSession') is not None:
            self.game_session = m.get('GameSession')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class StopGameSessionResponseBody(TeaModel):
    def __init__(
        self,
        game_id: str = None,
        game_session: str = None,
        message: str = None,
        queue_code: int = None,
        queue_state: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.game_id = game_id
        self.game_session = game_session
        self.message = message
        self.queue_code = queue_code
        self.queue_state = queue_state
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.game_session is not None:
            result['GameSession'] = self.game_session
        if self.message is not None:
            result['Message'] = self.message
        if self.queue_code is not None:
            result['QueueCode'] = self.queue_code
        if self.queue_state is not None:
            result['QueueState'] = self.queue_state
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('GameSession') is not None:
            self.game_session = m.get('GameSession')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('QueueCode') is not None:
            self.queue_code = m.get('QueueCode')
        if m.get('QueueState') is not None:
            self.queue_state = m.get('QueueState')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StopGameSessionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopGameSessionResponseBody = None,
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
            temp_model = StopGameSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitDeploymentRequest(TeaModel):
    def __init__(
        self,
        cloud_game_instance_ids: str = None,
        game_id: str = None,
        operation_type: str = None,
        project_id: str = None,
        version_id: str = None,
    ):
        # 实例ID列表
        self.cloud_game_instance_ids = cloud_game_instance_ids
        # 游戏iD
        self.game_id = game_id
        # 操作类型
        self.operation_type = operation_type
        # 项目ID
        self.project_id = project_id
        # 游戏版本ID
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_game_instance_ids is not None:
            result['CloudGameInstanceIds'] = self.cloud_game_instance_ids
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudGameInstanceIds') is not None:
            self.cloud_game_instance_ids = m.get('CloudGameInstanceIds')
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class SubmitDeploymentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 任务ID
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class SubmitDeploymentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SubmitDeploymentResponseBody = None,
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
            temp_model = SubmitDeploymentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitInternalPurchaseChargeDataRequest(TeaModel):
    def __init__(
        self,
        active_user_retention_rate_one_day: float = None,
        active_user_retention_rate_seven_day: float = None,
        active_user_retention_rate_thirty_day: float = None,
        arpu: float = None,
        charge_date: str = None,
        dau: int = None,
        game_id: str = None,
        mau: int = None,
        new_user_retention_rate_one_day: float = None,
        new_user_retention_rate_seven_day: float = None,
        new_user_retention_rate_thirty_day: float = None,
        payment_conversion_rate: float = None,
        play_time_average_one_day: float = None,
        play_time_average_thirty_day: float = None,
        play_time_ninety_points_one_day: float = None,
        play_time_ninety_points_thirty_day: float = None,
        play_time_range_one_day: str = None,
        play_time_range_thirty_day: str = None,
        user_activation_rate: float = None,
    ):
        self.active_user_retention_rate_one_day = active_user_retention_rate_one_day
        self.active_user_retention_rate_seven_day = active_user_retention_rate_seven_day
        self.active_user_retention_rate_thirty_day = active_user_retention_rate_thirty_day
        self.arpu = arpu
        self.charge_date = charge_date
        self.dau = dau
        self.game_id = game_id
        self.mau = mau
        self.new_user_retention_rate_one_day = new_user_retention_rate_one_day
        self.new_user_retention_rate_seven_day = new_user_retention_rate_seven_day
        self.new_user_retention_rate_thirty_day = new_user_retention_rate_thirty_day
        self.payment_conversion_rate = payment_conversion_rate
        self.play_time_average_one_day = play_time_average_one_day
        self.play_time_average_thirty_day = play_time_average_thirty_day
        self.play_time_ninety_points_one_day = play_time_ninety_points_one_day
        self.play_time_ninety_points_thirty_day = play_time_ninety_points_thirty_day
        self.play_time_range_one_day = play_time_range_one_day
        self.play_time_range_thirty_day = play_time_range_thirty_day
        self.user_activation_rate = user_activation_rate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_user_retention_rate_one_day is not None:
            result['ActiveUserRetentionRateOneDay'] = self.active_user_retention_rate_one_day
        if self.active_user_retention_rate_seven_day is not None:
            result['ActiveUserRetentionRateSevenDay'] = self.active_user_retention_rate_seven_day
        if self.active_user_retention_rate_thirty_day is not None:
            result['ActiveUserRetentionRateThirtyDay'] = self.active_user_retention_rate_thirty_day
        if self.arpu is not None:
            result['Arpu'] = self.arpu
        if self.charge_date is not None:
            result['ChargeDate'] = self.charge_date
        if self.dau is not None:
            result['Dau'] = self.dau
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.mau is not None:
            result['Mau'] = self.mau
        if self.new_user_retention_rate_one_day is not None:
            result['NewUserRetentionRateOneDay'] = self.new_user_retention_rate_one_day
        if self.new_user_retention_rate_seven_day is not None:
            result['NewUserRetentionRateSevenDay'] = self.new_user_retention_rate_seven_day
        if self.new_user_retention_rate_thirty_day is not None:
            result['NewUserRetentionRateThirtyDay'] = self.new_user_retention_rate_thirty_day
        if self.payment_conversion_rate is not None:
            result['PaymentConversionRate'] = self.payment_conversion_rate
        if self.play_time_average_one_day is not None:
            result['PlayTimeAverageOneDay'] = self.play_time_average_one_day
        if self.play_time_average_thirty_day is not None:
            result['PlayTimeAverageThirtyDay'] = self.play_time_average_thirty_day
        if self.play_time_ninety_points_one_day is not None:
            result['PlayTimeNinetyPointsOneDay'] = self.play_time_ninety_points_one_day
        if self.play_time_ninety_points_thirty_day is not None:
            result['PlayTimeNinetyPointsThirtyDay'] = self.play_time_ninety_points_thirty_day
        if self.play_time_range_one_day is not None:
            result['PlayTimeRangeOneDay'] = self.play_time_range_one_day
        if self.play_time_range_thirty_day is not None:
            result['PlayTimeRangeThirtyDay'] = self.play_time_range_thirty_day
        if self.user_activation_rate is not None:
            result['UserActivationRate'] = self.user_activation_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveUserRetentionRateOneDay') is not None:
            self.active_user_retention_rate_one_day = m.get('ActiveUserRetentionRateOneDay')
        if m.get('ActiveUserRetentionRateSevenDay') is not None:
            self.active_user_retention_rate_seven_day = m.get('ActiveUserRetentionRateSevenDay')
        if m.get('ActiveUserRetentionRateThirtyDay') is not None:
            self.active_user_retention_rate_thirty_day = m.get('ActiveUserRetentionRateThirtyDay')
        if m.get('Arpu') is not None:
            self.arpu = m.get('Arpu')
        if m.get('ChargeDate') is not None:
            self.charge_date = m.get('ChargeDate')
        if m.get('Dau') is not None:
            self.dau = m.get('Dau')
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('Mau') is not None:
            self.mau = m.get('Mau')
        if m.get('NewUserRetentionRateOneDay') is not None:
            self.new_user_retention_rate_one_day = m.get('NewUserRetentionRateOneDay')
        if m.get('NewUserRetentionRateSevenDay') is not None:
            self.new_user_retention_rate_seven_day = m.get('NewUserRetentionRateSevenDay')
        if m.get('NewUserRetentionRateThirtyDay') is not None:
            self.new_user_retention_rate_thirty_day = m.get('NewUserRetentionRateThirtyDay')
        if m.get('PaymentConversionRate') is not None:
            self.payment_conversion_rate = m.get('PaymentConversionRate')
        if m.get('PlayTimeAverageOneDay') is not None:
            self.play_time_average_one_day = m.get('PlayTimeAverageOneDay')
        if m.get('PlayTimeAverageThirtyDay') is not None:
            self.play_time_average_thirty_day = m.get('PlayTimeAverageThirtyDay')
        if m.get('PlayTimeNinetyPointsOneDay') is not None:
            self.play_time_ninety_points_one_day = m.get('PlayTimeNinetyPointsOneDay')
        if m.get('PlayTimeNinetyPointsThirtyDay') is not None:
            self.play_time_ninety_points_thirty_day = m.get('PlayTimeNinetyPointsThirtyDay')
        if m.get('PlayTimeRangeOneDay') is not None:
            self.play_time_range_one_day = m.get('PlayTimeRangeOneDay')
        if m.get('PlayTimeRangeThirtyDay') is not None:
            self.play_time_range_thirty_day = m.get('PlayTimeRangeThirtyDay')
        if m.get('UserActivationRate') is not None:
            self.user_activation_rate = m.get('UserActivationRate')
        return self


class SubmitInternalPurchaseChargeDataResponseBodyData(TeaModel):
    def __init__(
        self,
        message: str = None,
        status: int = None,
    ):
        self.message = message
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class SubmitInternalPurchaseChargeDataResponseBody(TeaModel):
    def __init__(
        self,
        data: SubmitInternalPurchaseChargeDataResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SubmitInternalPurchaseChargeDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitInternalPurchaseChargeDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SubmitInternalPurchaseChargeDataResponseBody = None,
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
            temp_model = SubmitInternalPurchaseChargeDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitInternalPurchaseOrdersRequestOrderList(TeaModel):
    def __init__(
        self,
        batch_number: str = None,
        final_price: int = None,
        finish_time: int = None,
        game_id: str = None,
        order_id: str = None,
        role_id: str = None,
        user_id: str = None,
    ):
        self.batch_number = batch_number
        self.final_price = final_price
        self.finish_time = finish_time
        self.game_id = game_id
        self.order_id = order_id
        self.role_id = role_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_number is not None:
            result['BatchNumber'] = self.batch_number
        if self.final_price is not None:
            result['FinalPrice'] = self.final_price
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchNumber') is not None:
            self.batch_number = m.get('BatchNumber')
        if m.get('FinalPrice') is not None:
            self.final_price = m.get('FinalPrice')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class SubmitInternalPurchaseOrdersRequest(TeaModel):
    def __init__(
        self,
        order_list: List[SubmitInternalPurchaseOrdersRequestOrderList] = None,
    ):
        self.order_list = order_list

    def validate(self):
        if self.order_list:
            for k in self.order_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OrderList'] = []
        if self.order_list is not None:
            for k in self.order_list:
                result['OrderList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.order_list = []
        if m.get('OrderList') is not None:
            for k in m.get('OrderList'):
                temp_model = SubmitInternalPurchaseOrdersRequestOrderList()
                self.order_list.append(temp_model.from_map(k))
        return self


class SubmitInternalPurchaseOrdersResponseBodyData(TeaModel):
    def __init__(
        self,
        message: str = None,
        status: int = None,
    ):
        self.message = message
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class SubmitInternalPurchaseOrdersResponseBody(TeaModel):
    def __init__(
        self,
        data: SubmitInternalPurchaseOrdersResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SubmitInternalPurchaseOrdersResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitInternalPurchaseOrdersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SubmitInternalPurchaseOrdersResponseBody = None,
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
            temp_model = SubmitInternalPurchaseOrdersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitInternalPurchaseReadyFlagRequestBatchInfoList(TeaModel):
    def __init__(
        self,
        batch_numbers: str = None,
        batch_size: int = None,
    ):
        self.batch_numbers = batch_numbers
        self.batch_size = batch_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_numbers is not None:
            result['BatchNumbers'] = self.batch_numbers
        if self.batch_size is not None:
            result['BatchSize'] = self.batch_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchNumbers') is not None:
            self.batch_numbers = m.get('BatchNumbers')
        if m.get('BatchSize') is not None:
            self.batch_size = m.get('BatchSize')
        return self


class SubmitInternalPurchaseReadyFlagRequest(TeaModel):
    def __init__(
        self,
        batch_info_list: List[SubmitInternalPurchaseReadyFlagRequestBatchInfoList] = None,
        charge_date: str = None,
        game_id: str = None,
        order_total_count: int = None,
        status: int = None,
    ):
        self.batch_info_list = batch_info_list
        self.charge_date = charge_date
        self.game_id = game_id
        self.order_total_count = order_total_count
        self.status = status

    def validate(self):
        if self.batch_info_list:
            for k in self.batch_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BatchInfoList'] = []
        if self.batch_info_list is not None:
            for k in self.batch_info_list:
                result['BatchInfoList'].append(k.to_map() if k else None)
        if self.charge_date is not None:
            result['ChargeDate'] = self.charge_date
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.order_total_count is not None:
            result['OrderTotalCount'] = self.order_total_count
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.batch_info_list = []
        if m.get('BatchInfoList') is not None:
            for k in m.get('BatchInfoList'):
                temp_model = SubmitInternalPurchaseReadyFlagRequestBatchInfoList()
                self.batch_info_list.append(temp_model.from_map(k))
        if m.get('ChargeDate') is not None:
            self.charge_date = m.get('ChargeDate')
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('OrderTotalCount') is not None:
            self.order_total_count = m.get('OrderTotalCount')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class SubmitInternalPurchaseReadyFlagResponseBodyData(TeaModel):
    def __init__(
        self,
        message: str = None,
        missing_batch_numbers: str = None,
        status: int = None,
    ):
        self.message = message
        self.missing_batch_numbers = missing_batch_numbers
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.missing_batch_numbers is not None:
            result['MissingBatchNumbers'] = self.missing_batch_numbers
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('MissingBatchNumbers') is not None:
            self.missing_batch_numbers = m.get('MissingBatchNumbers')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class SubmitInternalPurchaseReadyFlagResponseBody(TeaModel):
    def __init__(
        self,
        data: SubmitInternalPurchaseReadyFlagResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SubmitInternalPurchaseReadyFlagResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitInternalPurchaseReadyFlagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SubmitInternalPurchaseReadyFlagResponseBody = None,
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
            temp_model = SubmitInternalPurchaseReadyFlagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadGameVersionByDownloadRequest(TeaModel):
    def __init__(
        self,
        download_type: str = None,
        file_type: str = None,
        game_id: str = None,
        game_version: str = None,
        hash: str = None,
        version_name: str = None,
    ):
        self.download_type = download_type
        self.file_type = file_type
        self.game_id = game_id
        self.game_version = game_version
        self.hash = hash
        self.version_name = version_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.download_type is not None:
            result['DownloadType'] = self.download_type
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.game_version is not None:
            result['GameVersion'] = self.game_version
        if self.hash is not None:
            result['Hash'] = self.hash
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadType') is not None:
            self.download_type = m.get('DownloadType')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('GameVersion') is not None:
            self.game_version = m.get('GameVersion')
        if m.get('Hash') is not None:
            self.hash = m.get('Hash')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class UploadGameVersionByDownloadResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 任务id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class UploadGameVersionByDownloadResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UploadGameVersionByDownloadResponseBody = None,
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
            temp_model = UploadGameVersionByDownloadResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


