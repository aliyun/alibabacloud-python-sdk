# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class CancelVideoTaskRequestApp(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class CancelVideoTaskRequest(TeaModel):
    def __init__(
        self,
        app: CancelVideoTaskRequestApp = None,
        task_uuid: str = None,
        tenant_id: int = None,
    ):
        self.app = app
        self.task_uuid = task_uuid
        self.tenant_id = tenant_id

    def validate(self):
        if self.app:
            self.app.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app.to_map()
        if self.task_uuid is not None:
            result['TaskUuid'] = self.task_uuid
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            temp_model = CancelVideoTaskRequestApp()
            self.app = temp_model.from_map(m['App'])
        if m.get('TaskUuid') is not None:
            self.task_uuid = m.get('TaskUuid')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class CancelVideoTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        app_shrink: str = None,
        task_uuid: str = None,
        tenant_id: int = None,
    ):
        self.app_shrink = app_shrink
        self.task_uuid = task_uuid
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_shrink is not None:
            result['App'] = self.app_shrink
        if self.task_uuid is not None:
            result['TaskUuid'] = self.task_uuid
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app_shrink = m.get('App')
        if m.get('TaskUuid') is not None:
            self.task_uuid = m.get('TaskUuid')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class CancelVideoTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        fail_reason: str = None,
        is_cancel: bool = None,
        task_uuid: str = None,
    ):
        self.fail_reason = fail_reason
        self.is_cancel = is_cancel
        self.task_uuid = task_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail_reason is not None:
            result['FailReason'] = self.fail_reason
        if self.is_cancel is not None:
            result['IsCancel'] = self.is_cancel
        if self.task_uuid is not None:
            result['TaskUuid'] = self.task_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailReason') is not None:
            self.fail_reason = m.get('FailReason')
        if m.get('IsCancel') is not None:
            self.is_cancel = m.get('IsCancel')
        if m.get('TaskUuid') is not None:
            self.task_uuid = m.get('TaskUuid')
        return self


class CancelVideoTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CancelVideoTaskResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CancelVideoTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CancelVideoTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelVideoTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CancelVideoTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DuplexDecisionRequestDialogContextHistories(TeaModel):
    def __init__(
        self,
        robot: str = None,
        user: str = None,
    ):
        self.robot = robot
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.robot is not None:
            result['Robot'] = self.robot
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Robot') is not None:
            self.robot = m.get('Robot')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DuplexDecisionRequestDialogContext(TeaModel):
    def __init__(
        self,
        cur_utterance_idx: int = None,
        histories: List[DuplexDecisionRequestDialogContextHistories] = None,
    ):
        self.cur_utterance_idx = cur_utterance_idx
        self.histories = histories

    def validate(self):
        if self.histories:
            for k in self.histories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cur_utterance_idx is not None:
            result['CurUtteranceIdx'] = self.cur_utterance_idx
        result['Histories'] = []
        if self.histories is not None:
            for k in self.histories:
                result['Histories'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurUtteranceIdx') is not None:
            self.cur_utterance_idx = m.get('CurUtteranceIdx')
        self.histories = []
        if m.get('Histories') is not None:
            for k in m.get('Histories'):
                temp_model = DuplexDecisionRequestDialogContextHistories()
                self.histories.append(temp_model.from_map(k))
        return self


class DuplexDecisionRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        biz_request_id: str = None,
        call_time: int = None,
        custom_keywords: List[str] = None,
        dialog_context: DuplexDecisionRequestDialogContext = None,
        dialog_status: str = None,
        interrupt_type: int = None,
        session_id: str = None,
        tenant_id: int = None,
        text: str = None,
    ):
        self.app_id = app_id
        self.biz_request_id = biz_request_id
        self.call_time = call_time
        self.custom_keywords = custom_keywords
        self.dialog_context = dialog_context
        self.dialog_status = dialog_status
        self.interrupt_type = interrupt_type
        self.session_id = session_id
        self.tenant_id = tenant_id
        self.text = text

    def validate(self):
        if self.dialog_context:
            self.dialog_context.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.biz_request_id is not None:
            result['BizRequestId'] = self.biz_request_id
        if self.call_time is not None:
            result['CallTime'] = self.call_time
        if self.custom_keywords is not None:
            result['CustomKeywords'] = self.custom_keywords
        if self.dialog_context is not None:
            result['DialogContext'] = self.dialog_context.to_map()
        if self.dialog_status is not None:
            result['DialogStatus'] = self.dialog_status
        if self.interrupt_type is not None:
            result['InterruptType'] = self.interrupt_type
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BizRequestId') is not None:
            self.biz_request_id = m.get('BizRequestId')
        if m.get('CallTime') is not None:
            self.call_time = m.get('CallTime')
        if m.get('CustomKeywords') is not None:
            self.custom_keywords = m.get('CustomKeywords')
        if m.get('DialogContext') is not None:
            temp_model = DuplexDecisionRequestDialogContext()
            self.dialog_context = temp_model.from_map(m['DialogContext'])
        if m.get('DialogStatus') is not None:
            self.dialog_status = m.get('DialogStatus')
        if m.get('InterruptType') is not None:
            self.interrupt_type = m.get('InterruptType')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class DuplexDecisionShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        biz_request_id: str = None,
        call_time: int = None,
        custom_keywords_shrink: str = None,
        dialog_context_shrink: str = None,
        dialog_status: str = None,
        interrupt_type: int = None,
        session_id: str = None,
        tenant_id: int = None,
        text: str = None,
    ):
        self.app_id = app_id
        self.biz_request_id = biz_request_id
        self.call_time = call_time
        self.custom_keywords_shrink = custom_keywords_shrink
        self.dialog_context_shrink = dialog_context_shrink
        self.dialog_status = dialog_status
        self.interrupt_type = interrupt_type
        self.session_id = session_id
        self.tenant_id = tenant_id
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.biz_request_id is not None:
            result['BizRequestId'] = self.biz_request_id
        if self.call_time is not None:
            result['CallTime'] = self.call_time
        if self.custom_keywords_shrink is not None:
            result['CustomKeywords'] = self.custom_keywords_shrink
        if self.dialog_context_shrink is not None:
            result['DialogContext'] = self.dialog_context_shrink
        if self.dialog_status is not None:
            result['DialogStatus'] = self.dialog_status
        if self.interrupt_type is not None:
            result['InterruptType'] = self.interrupt_type
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BizRequestId') is not None:
            self.biz_request_id = m.get('BizRequestId')
        if m.get('CallTime') is not None:
            self.call_time = m.get('CallTime')
        if m.get('CustomKeywords') is not None:
            self.custom_keywords_shrink = m.get('CustomKeywords')
        if m.get('DialogContext') is not None:
            self.dialog_context_shrink = m.get('DialogContext')
        if m.get('DialogStatus') is not None:
            self.dialog_status = m.get('DialogStatus')
        if m.get('InterruptType') is not None:
            self.interrupt_type = m.get('InterruptType')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class DuplexDecisionResponseBodyData(TeaModel):
    def __init__(
        self,
        action_type: str = None,
        grab_type: str = None,
        output_text: str = None,
    ):
        self.action_type = action_type
        self.grab_type = grab_type
        self.output_text = output_text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.grab_type is not None:
            result['GrabType'] = self.grab_type
        if self.output_text is not None:
            result['OutputText'] = self.output_text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('GrabType') is not None:
            self.grab_type = m.get('GrabType')
        if m.get('OutputText') is not None:
            self.output_text = m.get('OutputText')
        return self


class DuplexDecisionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DuplexDecisionResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DuplexDecisionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DuplexDecisionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DuplexDecisionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DuplexDecisionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVideoTaskInfoRequestApp(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class GetVideoTaskInfoRequest(TeaModel):
    def __init__(
        self,
        app: GetVideoTaskInfoRequestApp = None,
        task_uuid: str = None,
        tenant_id: int = None,
    ):
        self.app = app
        self.task_uuid = task_uuid
        self.tenant_id = tenant_id

    def validate(self):
        if self.app:
            self.app.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app.to_map()
        if self.task_uuid is not None:
            result['TaskUuid'] = self.task_uuid
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            temp_model = GetVideoTaskInfoRequestApp()
            self.app = temp_model.from_map(m['App'])
        if m.get('TaskUuid') is not None:
            self.task_uuid = m.get('TaskUuid')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class GetVideoTaskInfoShrinkRequest(TeaModel):
    def __init__(
        self,
        app_shrink: str = None,
        task_uuid: str = None,
        tenant_id: int = None,
    ):
        self.app_shrink = app_shrink
        self.task_uuid = task_uuid
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_shrink is not None:
            result['App'] = self.app_shrink
        if self.task_uuid is not None:
            result['TaskUuid'] = self.task_uuid
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app_shrink = m.get('App')
        if m.get('TaskUuid') is not None:
            self.task_uuid = m.get('TaskUuid')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class GetVideoTaskInfoResponseBodyDataTaskResult(TeaModel):
    def __init__(
        self,
        fail_reason: str = None,
        subtitles_url: str = None,
        video_url: str = None,
    ):
        self.fail_reason = fail_reason
        self.subtitles_url = subtitles_url
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail_reason is not None:
            result['FailReason'] = self.fail_reason
        if self.subtitles_url is not None:
            result['SubtitlesUrl'] = self.subtitles_url
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailReason') is not None:
            self.fail_reason = m.get('FailReason')
        if m.get('SubtitlesUrl') is not None:
            self.subtitles_url = m.get('SubtitlesUrl')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class GetVideoTaskInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        process: str = None,
        status: str = None,
        task_result: GetVideoTaskInfoResponseBodyDataTaskResult = None,
        task_uuid: str = None,
        type: str = None,
    ):
        self.process = process
        self.status = status
        self.task_result = task_result
        self.task_uuid = task_uuid
        self.type = type

    def validate(self):
        if self.task_result:
            self.task_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.process is not None:
            result['Process'] = self.process
        if self.status is not None:
            result['Status'] = self.status
        if self.task_result is not None:
            result['TaskResult'] = self.task_result.to_map()
        if self.task_uuid is not None:
            result['TaskUuid'] = self.task_uuid
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Process') is not None:
            self.process = m.get('Process')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskResult') is not None:
            temp_model = GetVideoTaskInfoResponseBodyDataTaskResult()
            self.task_result = temp_model.from_map(m['TaskResult'])
        if m.get('TaskUuid') is not None:
            self.task_uuid = m.get('TaskUuid')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetVideoTaskInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetVideoTaskInfoResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetVideoTaskInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetVideoTaskInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetVideoTaskInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetVideoTaskInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRunningInstanceRequestApp(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class QueryRunningInstanceRequest(TeaModel):
    def __init__(
        self,
        app: QueryRunningInstanceRequestApp = None,
        session_id: str = None,
        tenant_id: int = None,
    ):
        self.app = app
        self.session_id = session_id
        self.tenant_id = tenant_id

    def validate(self):
        if self.app:
            self.app.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app.to_map()
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            temp_model = QueryRunningInstanceRequestApp()
            self.app = temp_model.from_map(m['App'])
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryRunningInstanceShrinkRequest(TeaModel):
    def __init__(
        self,
        app_shrink: str = None,
        session_id: str = None,
        tenant_id: int = None,
    ):
        self.app_shrink = app_shrink
        self.session_id = session_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_shrink is not None:
            result['App'] = self.app_shrink
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app_shrink = m.get('App')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryRunningInstanceResponseBodyDataChannel(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        expired_time: str = None,
        gslb: List[str] = None,
        nonce: str = None,
        token: str = None,
        type: str = None,
        user_id: str = None,
        user_info_in_channel: str = None,
    ):
        self.app_id = app_id
        self.channel_id = channel_id
        self.expired_time = expired_time
        self.gslb = gslb
        self.nonce = nonce
        self.token = token
        self.type = type
        self.user_id = user_id
        self.user_info_in_channel = user_info_in_channel

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.gslb is not None:
            result['Gslb'] = self.gslb
        if self.nonce is not None:
            result['Nonce'] = self.nonce
        if self.token is not None:
            result['Token'] = self.token
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_info_in_channel is not None:
            result['UserInfoInChannel'] = self.user_info_in_channel
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('Gslb') is not None:
            self.gslb = m.get('Gslb')
        if m.get('Nonce') is not None:
            self.nonce = m.get('Nonce')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserInfoInChannel') is not None:
            self.user_info_in_channel = m.get('UserInfoInChannel')
        return self


class QueryRunningInstanceResponseBodyDataUser(TeaModel):
    def __init__(
        self,
        user_id: str = None,
        user_name: str = None,
    ):
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class QueryRunningInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        channel: QueryRunningInstanceResponseBodyDataChannel = None,
        session_id: str = None,
        user: QueryRunningInstanceResponseBodyDataUser = None,
    ):
        self.channel = channel
        self.session_id = session_id
        self.user = user

    def validate(self):
        if self.channel:
            self.channel.validate()
        if self.user:
            self.user.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel.to_map()
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.user is not None:
            result['User'] = self.user.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            temp_model = QueryRunningInstanceResponseBodyDataChannel()
            self.channel = temp_model.from_map(m['Channel'])
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('User') is not None:
            temp_model = QueryRunningInstanceResponseBodyDataUser()
            self.user = temp_model.from_map(m['User'])
        return self


class QueryRunningInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[QueryRunningInstanceResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryRunningInstanceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRunningInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryRunningInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = QueryRunningInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendMessageRequestTextRequest(TeaModel):
    def __init__(
        self,
        command_type: str = None,
        id: str = None,
        speech_text: str = None,
        interrupt: bool = None,
    ):
        self.command_type = command_type
        self.id = id
        self.speech_text = speech_text
        self.interrupt = interrupt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command_type is not None:
            result['CommandType'] = self.command_type
        if self.id is not None:
            result['Id'] = self.id
        if self.speech_text is not None:
            result['SpeechText'] = self.speech_text
        if self.interrupt is not None:
            result['interrupt'] = self.interrupt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandType') is not None:
            self.command_type = m.get('CommandType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('SpeechText') is not None:
            self.speech_text = m.get('SpeechText')
        if m.get('interrupt') is not None:
            self.interrupt = m.get('interrupt')
        return self


class SendMessageRequestVAMLRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        vaml: str = None,
    ):
        self.code = code
        self.vaml = vaml

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.vaml is not None:
            result['Vaml'] = self.vaml
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Vaml') is not None:
            self.vaml = m.get('Vaml')
        return self


class SendMessageRequest(TeaModel):
    def __init__(
        self,
        session_id: str = None,
        tenant_id: int = None,
        text_request: SendMessageRequestTextRequest = None,
        vamlrequest: SendMessageRequestVAMLRequest = None,
    ):
        self.session_id = session_id
        self.tenant_id = tenant_id
        self.text_request = text_request
        self.vamlrequest = vamlrequest

    def validate(self):
        if self.text_request:
            self.text_request.validate()
        if self.vamlrequest:
            self.vamlrequest.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.text_request is not None:
            result['TextRequest'] = self.text_request.to_map()
        if self.vamlrequest is not None:
            result['VAMLRequest'] = self.vamlrequest.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('TextRequest') is not None:
            temp_model = SendMessageRequestTextRequest()
            self.text_request = temp_model.from_map(m['TextRequest'])
        if m.get('VAMLRequest') is not None:
            temp_model = SendMessageRequestVAMLRequest()
            self.vamlrequest = temp_model.from_map(m['VAMLRequest'])
        return self


class SendMessageShrinkRequest(TeaModel):
    def __init__(
        self,
        session_id: str = None,
        tenant_id: int = None,
        text_request_shrink: str = None,
        vamlrequest_shrink: str = None,
    ):
        self.session_id = session_id
        self.tenant_id = tenant_id
        self.text_request_shrink = text_request_shrink
        self.vamlrequest_shrink = vamlrequest_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.text_request_shrink is not None:
            result['TextRequest'] = self.text_request_shrink
        if self.vamlrequest_shrink is not None:
            result['VAMLRequest'] = self.vamlrequest_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('TextRequest') is not None:
            self.text_request_shrink = m.get('TextRequest')
        if m.get('VAMLRequest') is not None:
            self.vamlrequest_shrink = m.get('VAMLRequest')
        return self


class SendMessageResponseBodyData(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        session_id: str = None,
    ):
        self.request_id = request_id
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class SendMessageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SendMessageResponseBodyData = None,
        message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SendMessageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SendMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendMessageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = SendMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartInstanceRequestApp(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class StartInstanceRequestChannel(TeaModel):
    def __init__(
        self,
        req_config: Dict[str, Any] = None,
        type: str = None,
    ):
        self.req_config = req_config
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.req_config is not None:
            result['ReqConfig'] = self.req_config
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReqConfig') is not None:
            self.req_config = m.get('ReqConfig')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class StartInstanceRequestCommandRequest(TeaModel):
    def __init__(
        self,
        alpha_switch: bool = None,
    ):
        self.alpha_switch = alpha_switch

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alpha_switch is not None:
            result['AlphaSwitch'] = self.alpha_switch
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlphaSwitch') is not None:
            self.alpha_switch = m.get('AlphaSwitch')
        return self


class StartInstanceRequestUser(TeaModel):
    def __init__(
        self,
        user_id: str = None,
        user_name: str = None,
    ):
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class StartInstanceRequest(TeaModel):
    def __init__(
        self,
        app: StartInstanceRequestApp = None,
        channel: StartInstanceRequestChannel = None,
        command_request: StartInstanceRequestCommandRequest = None,
        tenant_id: int = None,
        user: StartInstanceRequestUser = None,
    ):
        self.app = app
        self.channel = channel
        self.command_request = command_request
        self.tenant_id = tenant_id
        self.user = user

    def validate(self):
        if self.app:
            self.app.validate()
        if self.channel:
            self.channel.validate()
        if self.command_request:
            self.command_request.validate()
        if self.user:
            self.user.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app.to_map()
        if self.channel is not None:
            result['Channel'] = self.channel.to_map()
        if self.command_request is not None:
            result['CommandRequest'] = self.command_request.to_map()
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.user is not None:
            result['User'] = self.user.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            temp_model = StartInstanceRequestApp()
            self.app = temp_model.from_map(m['App'])
        if m.get('Channel') is not None:
            temp_model = StartInstanceRequestChannel()
            self.channel = temp_model.from_map(m['Channel'])
        if m.get('CommandRequest') is not None:
            temp_model = StartInstanceRequestCommandRequest()
            self.command_request = temp_model.from_map(m['CommandRequest'])
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('User') is not None:
            temp_model = StartInstanceRequestUser()
            self.user = temp_model.from_map(m['User'])
        return self


class StartInstanceShrinkRequest(TeaModel):
    def __init__(
        self,
        app_shrink: str = None,
        channel_shrink: str = None,
        command_request_shrink: str = None,
        tenant_id: int = None,
        user_shrink: str = None,
    ):
        self.app_shrink = app_shrink
        self.channel_shrink = channel_shrink
        self.command_request_shrink = command_request_shrink
        self.tenant_id = tenant_id
        self.user_shrink = user_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_shrink is not None:
            result['App'] = self.app_shrink
        if self.channel_shrink is not None:
            result['Channel'] = self.channel_shrink
        if self.command_request_shrink is not None:
            result['CommandRequest'] = self.command_request_shrink
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.user_shrink is not None:
            result['User'] = self.user_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app_shrink = m.get('App')
        if m.get('Channel') is not None:
            self.channel_shrink = m.get('Channel')
        if m.get('CommandRequest') is not None:
            self.command_request_shrink = m.get('CommandRequest')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('User') is not None:
            self.user_shrink = m.get('User')
        return self


class StartInstanceResponseBodyDataChannel(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        expired_time: str = None,
        gslb: List[str] = None,
        nonce: str = None,
        token: str = None,
        type: str = None,
        user_id: str = None,
        user_info_in_channel: str = None,
    ):
        self.app_id = app_id
        self.channel_id = channel_id
        self.expired_time = expired_time
        self.gslb = gslb
        self.nonce = nonce
        self.token = token
        self.type = type
        self.user_id = user_id
        self.user_info_in_channel = user_info_in_channel

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.gslb is not None:
            result['Gslb'] = self.gslb
        if self.nonce is not None:
            result['Nonce'] = self.nonce
        if self.token is not None:
            result['Token'] = self.token
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_info_in_channel is not None:
            result['UserInfoInChannel'] = self.user_info_in_channel
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('Gslb') is not None:
            self.gslb = m.get('Gslb')
        if m.get('Nonce') is not None:
            self.nonce = m.get('Nonce')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserInfoInChannel') is not None:
            self.user_info_in_channel = m.get('UserInfoInChannel')
        return self


class StartInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        channel: StartInstanceResponseBodyDataChannel = None,
        request_id: str = None,
        session_id: str = None,
        token: str = None,
    ):
        self.channel = channel
        self.request_id = request_id
        self.session_id = session_id
        self.token = token

    def validate(self):
        if self.channel:
            self.channel.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            temp_model = StartInstanceResponseBodyDataChannel()
            self.channel = temp_model.from_map(m['Channel'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class StartInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: StartInstanceResponseBodyData = None,
        message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = StartInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = StartInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopInstanceRequest(TeaModel):
    def __init__(
        self,
        session_id: str = None,
        tenant_id: int = None,
    ):
        self.session_id = session_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class StopInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        session_id: str = None,
    ):
        self.request_id = request_id
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class StopInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: StopInstanceResponseBodyData = None,
        message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = StopInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StopInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = StopInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitTextTo2DAvatarVideoTaskRequestApp(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class SubmitTextTo2DAvatarVideoTaskRequestVideoInfo(TeaModel):
    def __init__(
        self,
        is_alpha: bool = None,
        is_subtitles: bool = None,
    ):
        self.is_alpha = is_alpha
        self.is_subtitles = is_subtitles

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_alpha is not None:
            result['IsAlpha'] = self.is_alpha
        if self.is_subtitles is not None:
            result['IsSubtitles'] = self.is_subtitles
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsAlpha') is not None:
            self.is_alpha = m.get('IsAlpha')
        if m.get('IsSubtitles') is not None:
            self.is_subtitles = m.get('IsSubtitles')
        return self


class SubmitTextTo2DAvatarVideoTaskRequest(TeaModel):
    def __init__(
        self,
        app: SubmitTextTo2DAvatarVideoTaskRequestApp = None,
        tenant_id: int = None,
        text: str = None,
        title: str = None,
        video_info: SubmitTextTo2DAvatarVideoTaskRequestVideoInfo = None,
    ):
        self.app = app
        self.tenant_id = tenant_id
        self.text = text
        self.title = title
        self.video_info = video_info

    def validate(self):
        if self.app:
            self.app.validate()
        if self.video_info:
            self.video_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app.to_map()
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.text is not None:
            result['Text'] = self.text
        if self.title is not None:
            result['Title'] = self.title
        if self.video_info is not None:
            result['VideoInfo'] = self.video_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            temp_model = SubmitTextTo2DAvatarVideoTaskRequestApp()
            self.app = temp_model.from_map(m['App'])
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('VideoInfo') is not None:
            temp_model = SubmitTextTo2DAvatarVideoTaskRequestVideoInfo()
            self.video_info = temp_model.from_map(m['VideoInfo'])
        return self


class SubmitTextTo2DAvatarVideoTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        app_shrink: str = None,
        tenant_id: int = None,
        text: str = None,
        title: str = None,
        video_info_shrink: str = None,
    ):
        self.app_shrink = app_shrink
        self.tenant_id = tenant_id
        self.text = text
        self.title = title
        self.video_info_shrink = video_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_shrink is not None:
            result['App'] = self.app_shrink
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.text is not None:
            result['Text'] = self.text
        if self.title is not None:
            result['Title'] = self.title
        if self.video_info_shrink is not None:
            result['VideoInfo'] = self.video_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app_shrink = m.get('App')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('VideoInfo') is not None:
            self.video_info_shrink = m.get('VideoInfo')
        return self


class SubmitTextTo2DAvatarVideoTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        task_uuid: str = None,
    ):
        self.task_uuid = task_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_uuid is not None:
            result['TaskUuid'] = self.task_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskUuid') is not None:
            self.task_uuid = m.get('TaskUuid')
        return self


class SubmitTextTo2DAvatarVideoTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitTextTo2DAvatarVideoTaskResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SubmitTextTo2DAvatarVideoTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitTextTo2DAvatarVideoTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitTextTo2DAvatarVideoTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = SubmitTextTo2DAvatarVideoTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitTextTo3DAvatarVideoTaskRequestApp(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class SubmitTextTo3DAvatarVideoTaskRequestVideoInfo(TeaModel):
    def __init__(
        self,
        is_alpha: bool = None,
        is_subtitles: bool = None,
        resolution: int = None,
    ):
        self.is_alpha = is_alpha
        self.is_subtitles = is_subtitles
        self.resolution = resolution

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_alpha is not None:
            result['IsAlpha'] = self.is_alpha
        if self.is_subtitles is not None:
            result['IsSubtitles'] = self.is_subtitles
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsAlpha') is not None:
            self.is_alpha = m.get('IsAlpha')
        if m.get('IsSubtitles') is not None:
            self.is_subtitles = m.get('IsSubtitles')
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        return self


class SubmitTextTo3DAvatarVideoTaskRequest(TeaModel):
    def __init__(
        self,
        app: SubmitTextTo3DAvatarVideoTaskRequestApp = None,
        tenant_id: int = None,
        text: str = None,
        title: str = None,
        video_info: SubmitTextTo3DAvatarVideoTaskRequestVideoInfo = None,
    ):
        self.app = app
        self.tenant_id = tenant_id
        self.text = text
        self.title = title
        self.video_info = video_info

    def validate(self):
        if self.app:
            self.app.validate()
        if self.video_info:
            self.video_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app.to_map()
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.text is not None:
            result['Text'] = self.text
        if self.title is not None:
            result['Title'] = self.title
        if self.video_info is not None:
            result['VideoInfo'] = self.video_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            temp_model = SubmitTextTo3DAvatarVideoTaskRequestApp()
            self.app = temp_model.from_map(m['App'])
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('VideoInfo') is not None:
            temp_model = SubmitTextTo3DAvatarVideoTaskRequestVideoInfo()
            self.video_info = temp_model.from_map(m['VideoInfo'])
        return self


class SubmitTextTo3DAvatarVideoTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        app_shrink: str = None,
        tenant_id: int = None,
        text: str = None,
        title: str = None,
        video_info_shrink: str = None,
    ):
        self.app_shrink = app_shrink
        self.tenant_id = tenant_id
        self.text = text
        self.title = title
        self.video_info_shrink = video_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_shrink is not None:
            result['App'] = self.app_shrink
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.text is not None:
            result['Text'] = self.text
        if self.title is not None:
            result['Title'] = self.title
        if self.video_info_shrink is not None:
            result['VideoInfo'] = self.video_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app_shrink = m.get('App')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('VideoInfo') is not None:
            self.video_info_shrink = m.get('VideoInfo')
        return self


class SubmitTextTo3DAvatarVideoTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        task_uuid: str = None,
    ):
        self.task_uuid = task_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_uuid is not None:
            result['TaskUuid'] = self.task_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskUuid') is not None:
            self.task_uuid = m.get('TaskUuid')
        return self


class SubmitTextTo3DAvatarVideoTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitTextTo3DAvatarVideoTaskResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SubmitTextTo3DAvatarVideoTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitTextTo3DAvatarVideoTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitTextTo3DAvatarVideoTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = SubmitTextTo3DAvatarVideoTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitTextToSignVideoTaskRequestApp(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class SubmitTextToSignVideoTaskRequestVideoInfo(TeaModel):
    def __init__(
        self,
        is_alpha: bool = None,
        is_subtitles: bool = None,
        resolution: int = None,
    ):
        self.is_alpha = is_alpha
        self.is_subtitles = is_subtitles
        self.resolution = resolution

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_alpha is not None:
            result['IsAlpha'] = self.is_alpha
        if self.is_subtitles is not None:
            result['IsSubtitles'] = self.is_subtitles
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsAlpha') is not None:
            self.is_alpha = m.get('IsAlpha')
        if m.get('IsSubtitles') is not None:
            self.is_subtitles = m.get('IsSubtitles')
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        return self


class SubmitTextToSignVideoTaskRequest(TeaModel):
    def __init__(
        self,
        app: SubmitTextToSignVideoTaskRequestApp = None,
        tenant_id: int = None,
        text: str = None,
        title: str = None,
        video_info: SubmitTextToSignVideoTaskRequestVideoInfo = None,
    ):
        self.app = app
        self.tenant_id = tenant_id
        self.text = text
        self.title = title
        self.video_info = video_info

    def validate(self):
        if self.app:
            self.app.validate()
        if self.video_info:
            self.video_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app.to_map()
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.text is not None:
            result['Text'] = self.text
        if self.title is not None:
            result['Title'] = self.title
        if self.video_info is not None:
            result['VideoInfo'] = self.video_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            temp_model = SubmitTextToSignVideoTaskRequestApp()
            self.app = temp_model.from_map(m['App'])
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('VideoInfo') is not None:
            temp_model = SubmitTextToSignVideoTaskRequestVideoInfo()
            self.video_info = temp_model.from_map(m['VideoInfo'])
        return self


class SubmitTextToSignVideoTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        app_shrink: str = None,
        tenant_id: int = None,
        text: str = None,
        title: str = None,
        video_info_shrink: str = None,
    ):
        self.app_shrink = app_shrink
        self.tenant_id = tenant_id
        self.text = text
        self.title = title
        self.video_info_shrink = video_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_shrink is not None:
            result['App'] = self.app_shrink
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.text is not None:
            result['Text'] = self.text
        if self.title is not None:
            result['Title'] = self.title
        if self.video_info_shrink is not None:
            result['VideoInfo'] = self.video_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app_shrink = m.get('App')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('VideoInfo') is not None:
            self.video_info_shrink = m.get('VideoInfo')
        return self


class SubmitTextToSignVideoTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        task_uuid: str = None,
    ):
        self.task_uuid = task_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_uuid is not None:
            result['TaskUuid'] = self.task_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskUuid') is not None:
            self.task_uuid = m.get('TaskUuid')
        return self


class SubmitTextToSignVideoTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitTextToSignVideoTaskResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SubmitTextToSignVideoTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitTextToSignVideoTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitTextToSignVideoTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = SubmitTextToSignVideoTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


