# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class ActualDeductResourceCmd(TeaModel):
    def __init__(
        self,
        cost: int = None,
        extra_info: str = None,
        idempotent_id: str = None,
        task_id: str = None,
    ):
        self.cost = cost
        self.extra_info = extra_info
        self.idempotent_id = idempotent_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.extra_info is not None:
            result['extraInfo'] = self.extra_info
        if self.idempotent_id is not None:
            result['idempotentId'] = self.idempotent_id
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('extraInfo') is not None:
            self.extra_info = m.get('extraInfo')
        if m.get('idempotentId') is not None:
            self.idempotent_id = m.get('idempotentId')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class ActualDeductResourceResult(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DigitalHumanLiveBroadcastQACmdHistory(TeaModel):
    def __init__(
        self,
        bot: str = None,
        user: str = None,
    ):
        self.bot = bot
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bot is not None:
            result['bot'] = self.bot
        if self.user is not None:
            result['user'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bot') is not None:
            self.bot = m.get('bot')
        if m.get('user') is not None:
            self.user = m.get('user')
        return self


class DigitalHumanLiveBroadcastQACmd(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        history: List[DigitalHumanLiveBroadcastQACmdHistory] = None,
        question: str = None,
        session_id: str = None,
        stream: bool = None,
        sub_account_id: str = None,
    ):
        self.account_id = account_id
        self.history = history
        self.question = question
        self.session_id = session_id
        self.stream = stream
        self.sub_account_id = sub_account_id

    def validate(self):
        if self.history:
            for k in self.history:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        result['history'] = []
        if self.history is not None:
            for k in self.history:
                result['history'].append(k.to_map() if k else None)
        if self.question is not None:
            result['question'] = self.question
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.stream is not None:
            result['stream'] = self.stream
        if self.sub_account_id is not None:
            result['subAccountId'] = self.sub_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        self.history = []
        if m.get('history') is not None:
            for k in m.get('history'):
                temp_model = DigitalHumanLiveBroadcastQACmdHistory()
                self.history.append(temp_model.from_map(k))
        if m.get('question') is not None:
            self.question = m.get('question')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('stream') is not None:
            self.stream = m.get('stream')
        if m.get('subAccountId') is not None:
            self.sub_account_id = m.get('subAccountId')
        return self


class DigitalHumanLiveBroadcastQAResult(TeaModel):
    def __init__(
        self,
        content: str = None,
        error_code: str = None,
        error_message: str = None,
        session_id: str = None,
        success: bool = None,
    ):
        self.content = content
        self.error_code = error_code
        self.error_message = error_message
        self.session_id = session_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DirectDeductResourceCmd(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        cost: int = None,
        deduct_scene: str = None,
        extra_info: str = None,
        idempotent_id: str = None,
        resource_type: int = None,
        sub_account_id: str = None,
        token: str = None,
    ):
        self.account_id = account_id
        self.cost = cost
        self.deduct_scene = deduct_scene
        self.extra_info = extra_info
        self.idempotent_id = idempotent_id
        self.resource_type = resource_type
        self.sub_account_id = sub_account_id
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.cost is not None:
            result['cost'] = self.cost
        if self.deduct_scene is not None:
            result['deductScene'] = self.deduct_scene
        if self.extra_info is not None:
            result['extraInfo'] = self.extra_info
        if self.idempotent_id is not None:
            result['idempotentId'] = self.idempotent_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.sub_account_id is not None:
            result['subAccountId'] = self.sub_account_id
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('deductScene') is not None:
            self.deduct_scene = m.get('deductScene')
        if m.get('extraInfo') is not None:
            self.extra_info = m.get('extraInfo')
        if m.get('idempotentId') is not None:
            self.idempotent_id = m.get('idempotentId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('subAccountId') is not None:
            self.sub_account_id = m.get('subAccountId')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self


class DirectDeductResourceResult(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ExpectDeductResourceCmd(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        cost: int = None,
        deduct_scene: str = None,
        extra_info: str = None,
        idempotent_id: str = None,
        resource_type: int = None,
        sub_account_id: str = None,
        token: str = None,
    ):
        self.account_id = account_id
        self.cost = cost
        self.deduct_scene = deduct_scene
        self.extra_info = extra_info
        self.idempotent_id = idempotent_id
        self.resource_type = resource_type
        self.sub_account_id = sub_account_id
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.cost is not None:
            result['cost'] = self.cost
        if self.deduct_scene is not None:
            result['deductScene'] = self.deduct_scene
        if self.extra_info is not None:
            result['extraInfo'] = self.extra_info
        if self.idempotent_id is not None:
            result['idempotentId'] = self.idempotent_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.sub_account_id is not None:
            result['subAccountId'] = self.sub_account_id
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('deductScene') is not None:
            self.deduct_scene = m.get('deductScene')
        if m.get('extraInfo') is not None:
            self.extra_info = m.get('extraInfo')
        if m.get('idempotentId') is not None:
            self.idempotent_id = m.get('idempotentId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('subAccountId') is not None:
            self.sub_account_id = m.get('subAccountId')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self


class ExpectDeductResourceResult(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class SubmitBulletQuestionsCmdQuestions(TeaModel):
    def __init__(
        self,
        content: str = None,
        id: str = None,
        time: int = None,
        username: str = None,
    ):
        self.content = content
        self.id = id
        self.time = time
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.id is not None:
            result['id'] = self.id
        if self.time is not None:
            result['time'] = self.time
        if self.username is not None:
            result['username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('username') is not None:
            self.username = m.get('username')
        return self


class SubmitBulletQuestionsCmd(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        questions: List[SubmitBulletQuestionsCmdQuestions] = None,
        room_id: str = None,
        sub_account_id: str = None,
    ):
        self.account_id = account_id
        self.questions = questions
        self.room_id = room_id
        self.sub_account_id = sub_account_id

    def validate(self):
        if self.questions:
            for k in self.questions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        result['questions'] = []
        if self.questions is not None:
            for k in self.questions:
                result['questions'].append(k.to_map() if k else None)
        if self.room_id is not None:
            result['roomId'] = self.room_id
        if self.sub_account_id is not None:
            result['subAccountId'] = self.sub_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        self.questions = []
        if m.get('questions') is not None:
            for k in m.get('questions'):
                temp_model = SubmitBulletQuestionsCmdQuestions()
                self.questions.append(temp_model.from_map(k))
        if m.get('roomId') is not None:
            self.room_id = m.get('roomId')
        if m.get('subAccountId') is not None:
            self.sub_account_id = m.get('subAccountId')
        return self


class SubmitBulletQuestionsQAResult(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ActualDeductResourceRequest(TeaModel):
    def __init__(
        self,
        body: ActualDeductResourceCmd = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = ActualDeductResourceCmd()
            self.body = temp_model.from_map(m['body'])
        return self


class ActualDeductResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ActualDeductResourceResult = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ActualDeductResourceResult()
            self.body = temp_model.from_map(m['body'])
        return self


class ActualDeductResourcesRequest(TeaModel):
    def __init__(
        self,
        body: ActualDeductResourceCmd = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = ActualDeductResourceCmd()
            self.body = temp_model.from_map(m['body'])
        return self


class ActualDeductResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ActualDeductResourceResult = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ActualDeductResourceResult()
            self.body = temp_model.from_map(m['body'])
        return self


class CopywritingQARequestHistories(TeaModel):
    def __init__(
        self,
        bot: str = None,
        user: str = None,
    ):
        self.bot = bot
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bot is not None:
            result['bot'] = self.bot
        if self.user is not None:
            result['user'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bot') is not None:
            self.bot = m.get('bot')
        if m.get('user') is not None:
            self.user = m.get('user')
        return self


class CopywritingQARequestHistory(TeaModel):
    def __init__(
        self,
        bot: str = None,
        user: str = None,
    ):
        self.bot = bot
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bot is not None:
            result['bot'] = self.bot
        if self.user is not None:
            result['user'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bot') is not None:
            self.bot = m.get('bot')
        if m.get('user') is not None:
            self.user = m.get('user')
        return self


class CopywritingQARequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        histories: List[CopywritingQARequestHistories] = None,
        history: CopywritingQARequestHistory = None,
        question: str = None,
        session_id: str = None,
        stream: bool = None,
        sub_account_id: str = None,
    ):
        self.account_id = account_id
        self.histories = histories
        self.history = history
        self.question = question
        self.session_id = session_id
        self.stream = stream
        self.sub_account_id = sub_account_id

    def validate(self):
        if self.histories:
            for k in self.histories:
                if k:
                    k.validate()
        if self.history:
            self.history.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        result['histories'] = []
        if self.histories is not None:
            for k in self.histories:
                result['histories'].append(k.to_map() if k else None)
        if self.history is not None:
            result['history'] = self.history.to_map()
        if self.question is not None:
            result['question'] = self.question
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.stream is not None:
            result['stream'] = self.stream
        if self.sub_account_id is not None:
            result['subAccountId'] = self.sub_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        self.histories = []
        if m.get('histories') is not None:
            for k in m.get('histories'):
                temp_model = CopywritingQARequestHistories()
                self.histories.append(temp_model.from_map(k))
        if m.get('history') is not None:
            temp_model = CopywritingQARequestHistory()
            self.history = temp_model.from_map(m['history'])
        if m.get('question') is not None:
            self.question = m.get('question')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('stream') is not None:
            self.stream = m.get('stream')
        if m.get('subAccountId') is not None:
            self.sub_account_id = m.get('subAccountId')
        return self


class CopywritingQAShrinkRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        histories_shrink: str = None,
        history_shrink: str = None,
        question: str = None,
        session_id: str = None,
        stream: bool = None,
        sub_account_id: str = None,
    ):
        self.account_id = account_id
        self.histories_shrink = histories_shrink
        self.history_shrink = history_shrink
        self.question = question
        self.session_id = session_id
        self.stream = stream
        self.sub_account_id = sub_account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.histories_shrink is not None:
            result['histories'] = self.histories_shrink
        if self.history_shrink is not None:
            result['history'] = self.history_shrink
        if self.question is not None:
            result['question'] = self.question
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.stream is not None:
            result['stream'] = self.stream
        if self.sub_account_id is not None:
            result['subAccountId'] = self.sub_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('histories') is not None:
            self.histories_shrink = m.get('histories')
        if m.get('history') is not None:
            self.history_shrink = m.get('history')
        if m.get('question') is not None:
            self.question = m.get('question')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('stream') is not None:
            self.stream = m.get('stream')
        if m.get('subAccountId') is not None:
            self.sub_account_id = m.get('subAccountId')
        return self


class CopywritingQAResponseBody(TeaModel):
    def __init__(
        self,
        content: str = None,
        error_code: str = None,
        error_message: str = None,
        session_id: str = None,
        success: bool = None,
    ):
        self.content = content
        self.error_code = error_code
        self.error_message = error_message
        self.session_id = session_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CopywritingQAResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CopywritingQAResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CopywritingQAResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CopywritingQAV1Request(TeaModel):
    def __init__(
        self,
        body: DigitalHumanLiveBroadcastQACmd = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = DigitalHumanLiveBroadcastQACmd()
            self.body = temp_model.from_map(m['body'])
        return self


class CopywritingQAV1Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DigitalHumanLiveBroadcastQAResult = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DigitalHumanLiveBroadcastQAResult()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDigitalVideoRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        video_id: str = None,
    ):
        self.account_id = account_id
        self.video_id = video_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.video_id is not None:
            result['videoId'] = self.video_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('videoId') is not None:
            self.video_id = m.get('videoId')
        return self


class DeleteDigitalVideoResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteDigitalVideoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDigitalVideoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDigitalVideoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DirectDeductResourceRequest(TeaModel):
    def __init__(
        self,
        body: DirectDeductResourceCmd = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = DirectDeductResourceCmd()
            self.body = temp_model.from_map(m['body'])
        return self


class DirectDeductResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DirectDeductResourceResult = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DirectDeductResourceResult()
            self.body = temp_model.from_map(m['body'])
        return self


class DirectDeductResourcesRequest(TeaModel):
    def __init__(
        self,
        body: DirectDeductResourceCmd = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = DirectDeductResourceCmd()
            self.body = temp_model.from_map(m['body'])
        return self


class DirectDeductResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DirectDeductResourceResult = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DirectDeductResourceResult()
            self.body = temp_model.from_map(m['body'])
        return self


class ExpectDeductResourceRequest(TeaModel):
    def __init__(
        self,
        body: ExpectDeductResourceCmd = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = ExpectDeductResourceCmd()
            self.body = temp_model.from_map(m['body'])
        return self


class ExpectDeductResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExpectDeductResourceResult = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ExpectDeductResourceResult()
            self.body = temp_model.from_map(m['body'])
        return self


class ExpectDeductResourcesRequest(TeaModel):
    def __init__(
        self,
        body: ExpectDeductResourceCmd = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = ExpectDeductResourceCmd()
            self.body = temp_model.from_map(m['body'])
        return self


class ExpectDeductResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExpectDeductResourceResult = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ExpectDeductResourceResult()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRemainResourceRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        resource_type: str = None,
        sub_account_id: str = None,
    ):
        self.account_id = account_id
        self.resource_type = resource_type
        self.sub_account_id = sub_account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.sub_account_id is not None:
            result['subAccountId'] = self.sub_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('subAccountId') is not None:
            self.sub_account_id = m.get('subAccountId')
        return self


class GetRemainResourceResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        remain_count: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.remain_count = remain_count
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.remain_count is not None:
            result['remainCount'] = self.remain_count
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('remainCount') is not None:
            self.remain_count = m.get('remainCount')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetRemainResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRemainResourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRemainResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitBulletQuestionsRequestQuestions(TeaModel):
    def __init__(
        self,
        content: str = None,
        id: str = None,
        time: int = None,
        username: str = None,
    ):
        self.content = content
        self.id = id
        self.time = time
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.id is not None:
            result['id'] = self.id
        if self.time is not None:
            result['time'] = self.time
        if self.username is not None:
            result['username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('username') is not None:
            self.username = m.get('username')
        return self


class SubmitBulletQuestionsRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        questions: List[SubmitBulletQuestionsRequestQuestions] = None,
        room_id: str = None,
        sub_account_id: str = None,
    ):
        self.account_id = account_id
        # questions
        self.questions = questions
        self.room_id = room_id
        self.sub_account_id = sub_account_id

    def validate(self):
        if self.questions:
            for k in self.questions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        result['questions'] = []
        if self.questions is not None:
            for k in self.questions:
                result['questions'].append(k.to_map() if k else None)
        if self.room_id is not None:
            result['roomId'] = self.room_id
        if self.sub_account_id is not None:
            result['subAccountId'] = self.sub_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        self.questions = []
        if m.get('questions') is not None:
            for k in m.get('questions'):
                temp_model = SubmitBulletQuestionsRequestQuestions()
                self.questions.append(temp_model.from_map(k))
        if m.get('roomId') is not None:
            self.room_id = m.get('roomId')
        if m.get('subAccountId') is not None:
            self.sub_account_id = m.get('subAccountId')
        return self


class SubmitBulletQuestionsShrinkRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        questions_shrink: str = None,
        room_id: str = None,
        sub_account_id: str = None,
    ):
        self.account_id = account_id
        # questions
        self.questions_shrink = questions_shrink
        self.room_id = room_id
        self.sub_account_id = sub_account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.questions_shrink is not None:
            result['questions'] = self.questions_shrink
        if self.room_id is not None:
            result['roomId'] = self.room_id
        if self.sub_account_id is not None:
            result['subAccountId'] = self.sub_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('questions') is not None:
            self.questions_shrink = m.get('questions')
        if m.get('roomId') is not None:
            self.room_id = m.get('roomId')
        if m.get('subAccountId') is not None:
            self.sub_account_id = m.get('subAccountId')
        return self


class SubmitBulletQuestionsResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class SubmitBulletQuestionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitBulletQuestionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SubmitBulletQuestionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitBulletQuestionsV1Request(TeaModel):
    def __init__(
        self,
        body: SubmitBulletQuestionsCmd = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = SubmitBulletQuestionsCmd()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitBulletQuestionsV1Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitBulletQuestionsQAResult = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SubmitBulletQuestionsQAResult()
            self.body = temp_model.from_map(m['body'])
        return self


