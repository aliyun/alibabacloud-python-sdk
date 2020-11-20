# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
try:
    from typing import Dict, Any, List
except ImportError:
    pass


class SaveHotspotConfigRequest(TeaModel):
    def __init__(self, param_tag=None, preview_token=None):
        self.param_tag = param_tag      # type: str
        self.preview_token = preview_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ParamTag'] = self.param_tag
        result['PreviewToken'] = self.preview_token
        return result

    def from_map(self, map={}):
        self.param_tag = map.get('ParamTag')
        self.preview_token = map.get('PreviewToken')
        return self


class SaveHotspotConfigResponse(TeaModel):
    def __init__(self, request_id=None, success=None, err_message=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.err_message = err_message  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.err_message, 'err_message')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['ErrMessage'] = self.err_message
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.err_message = map.get('ErrMessage')
        return self


class GetHotspotConfigRequest(TeaModel):
    def __init__(self, preview_token=None):
        self.preview_token = preview_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['PreviewToken'] = self.preview_token
        return result

    def from_map(self, map={}):
        self.preview_token = map.get('PreviewToken')
        return self


class GetHotspotConfigResponse(TeaModel):
    def __init__(self, request_id=None, success=None, err_message=None, data=None, object_string=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.err_message = err_message  # type: str
        self.data = data                # type: str
        self.object_string = object_string  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.err_message, 'err_message')
        self.validate_required(self.data, 'data')
        self.validate_required(self.object_string, 'object_string')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['ErrMessage'] = self.err_message
        result['Data'] = self.data
        result['ObjectString'] = self.object_string
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.err_message = map.get('ErrMessage')
        self.data = map.get('Data')
        self.object_string = map.get('ObjectString')
        return self


class ListMainScenesRequest(TeaModel):
    def __init__(self, query_name=None):
        self.query_name = query_name    # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['QueryName'] = self.query_name
        return result

    def from_map(self, map={}):
        self.query_name = map.get('QueryName')
        return self


class ListMainScenesResponse(TeaModel):
    def __init__(self, request_id=None, success=None, err_message=None, data=None, object_string=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.err_message = err_message  # type: str
        self.data = data                # type: str
        self.object_string = object_string  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.err_message, 'err_message')
        self.validate_required(self.data, 'data')
        self.validate_required(self.object_string, 'object_string')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['ErrMessage'] = self.err_message
        result['Data'] = self.data
        result['ObjectString'] = self.object_string
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.err_message = map.get('ErrMessage')
        self.data = map.get('Data')
        self.object_string = map.get('ObjectString')
        return self


class SaveHotspotTagRequest(TeaModel):
    def __init__(self, param_tag=None, sub_scene_uuid=None):
        self.param_tag = param_tag      # type: str
        self.sub_scene_uuid = sub_scene_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ParamTag'] = self.param_tag
        result['SubSceneUuid'] = self.sub_scene_uuid
        return result

    def from_map(self, map={}):
        self.param_tag = map.get('ParamTag')
        self.sub_scene_uuid = map.get('SubSceneUuid')
        return self


class SaveHotspotTagResponse(TeaModel):
    def __init__(self, request_id=None, success=None, err_message=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.err_message = err_message  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.err_message, 'err_message')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['ErrMessage'] = self.err_message
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.err_message = map.get('ErrMessage')
        return self


class GetSceneListRequest(TeaModel):
    def __init__(self, account_id=None):
        self.account_id = account_id    # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['AccountId'] = self.account_id
        return result

    def from_map(self, map={}):
        self.account_id = map.get('AccountId')
        return self


class GetSceneListResponse(TeaModel):
    def __init__(self, request_id=None, success=None, err_message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.err_message = err_message  # type: str
        self.data = data                # type: Dict[str, Any]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.err_message, 'err_message')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['ErrMessage'] = self.err_message
        result['Data'] = self.data
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.err_message = map.get('ErrMessage')
        self.data = map.get('Data')
        return self


class SaveFileRequest(TeaModel):
    def __init__(self, param_file=None, sub_scene_uuid=None):
        self.param_file = param_file    # type: str
        self.sub_scene_uuid = sub_scene_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ParamFile'] = self.param_file
        result['SubSceneUuid'] = self.sub_scene_uuid
        return result

    def from_map(self, map={}):
        self.param_file = map.get('ParamFile')
        self.sub_scene_uuid = map.get('SubSceneUuid')
        return self


class SaveFileResponse(TeaModel):
    def __init__(self, request_id=None, success=None, err_message=None, data=None, object_string=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.err_message = err_message  # type: str
        self.data = data                # type: str
        self.object_string = object_string  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.err_message, 'err_message')
        self.validate_required(self.data, 'data')
        self.validate_required(self.object_string, 'object_string')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['ErrMessage'] = self.err_message
        result['Data'] = self.data
        result['ObjectString'] = self.object_string
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.err_message = map.get('ErrMessage')
        self.data = map.get('Data')
        self.object_string = map.get('ObjectString')
        return self


class DeleteFileRequest(TeaModel):
    def __init__(self, param_file=None, sub_scene_uuid=None):
        self.param_file = param_file    # type: str
        self.sub_scene_uuid = sub_scene_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ParamFile'] = self.param_file
        result['SubSceneUuid'] = self.sub_scene_uuid
        return result

    def from_map(self, map={}):
        self.param_file = map.get('ParamFile')
        self.sub_scene_uuid = map.get('SubSceneUuid')
        return self


class DeleteFileResponse(TeaModel):
    def __init__(self, request_id=None, success=None, err_message=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.err_message = err_message  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.err_message, 'err_message')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['ErrMessage'] = self.err_message
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.err_message = map.get('ErrMessage')
        return self


class GetHotspotTagRequest(TeaModel):
    def __init__(self, preview_token=None, sub_scene_uuid=None, type=None):
        self.preview_token = preview_token  # type: str
        self.sub_scene_uuid = sub_scene_uuid  # type: str
        self.type = type                # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['PreviewToken'] = self.preview_token
        result['SubSceneUuid'] = self.sub_scene_uuid
        result['Type'] = self.type
        return result

    def from_map(self, map={}):
        self.preview_token = map.get('PreviewToken')
        self.sub_scene_uuid = map.get('SubSceneUuid')
        self.type = map.get('Type')
        return self


class GetHotspotTagResponse(TeaModel):
    def __init__(self, request_id=None, success=None, err_message=None, data=None, object_string=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.err_message = err_message  # type: str
        self.data = data                # type: str
        self.object_string = object_string  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.err_message, 'err_message')
        self.validate_required(self.data, 'data')
        self.validate_required(self.object_string, 'object_string')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['ErrMessage'] = self.err_message
        result['Data'] = self.data
        result['ObjectString'] = self.object_string
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.err_message = map.get('ErrMessage')
        self.data = map.get('Data')
        self.object_string = map.get('ObjectString')
        return self


class GetPolicyRequest(TeaModel):
    def __init__(self, sub_scene_uuid=None, type=None):
        self.sub_scene_uuid = sub_scene_uuid  # type: str
        self.type = type                # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['SubSceneUuid'] = self.sub_scene_uuid
        result['Type'] = self.type
        return result

    def from_map(self, map={}):
        self.sub_scene_uuid = map.get('SubSceneUuid')
        self.type = map.get('Type')
        return self


class GetPolicyResponse(TeaModel):
    def __init__(self, request_id=None, success=None, err_message=None, data=None, object_string=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.err_message = err_message  # type: str
        self.data = data                # type: Dict[str, Any]
        self.object_string = object_string  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.err_message, 'err_message')
        self.validate_required(self.data, 'data')
        self.validate_required(self.object_string, 'object_string')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['ErrMessage'] = self.err_message
        result['Data'] = self.data
        result['ObjectString'] = self.object_string
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.err_message = map.get('ErrMessage')
        self.data = map.get('Data')
        self.object_string = map.get('ObjectString')
        return self


class PublishHotspotRequest(TeaModel):
    def __init__(self, param_tag=None, sub_scene_uuid=None):
        self.param_tag = param_tag      # type: str
        self.sub_scene_uuid = sub_scene_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ParamTag'] = self.param_tag
        result['SubSceneUuid'] = self.sub_scene_uuid
        return result

    def from_map(self, map={}):
        self.param_tag = map.get('ParamTag')
        self.sub_scene_uuid = map.get('SubSceneUuid')
        return self


class PublishHotspotResponse(TeaModel):
    def __init__(self, request_id=None, success=None, err_message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.err_message = err_message  # type: str
        self.data = data                # type: Dict[str, Any]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.err_message, 'err_message')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['ErrMessage'] = self.err_message
        result['Data'] = self.data
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.err_message = map.get('ErrMessage')
        self.data = map.get('Data')
        return self


class GetWindowConfigRequest(TeaModel):
    def __init__(self, preview_token=None):
        self.preview_token = preview_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['PreviewToken'] = self.preview_token
        return result

    def from_map(self, map={}):
        self.preview_token = map.get('PreviewToken')
        return self


class GetWindowConfigResponse(TeaModel):
    def __init__(self, request_id=None, success=None, err_message=None, data=None, object_string=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.err_message = err_message  # type: str
        self.data = data                # type: Dict[str, Any]
        self.object_string = object_string  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.err_message, 'err_message')
        self.validate_required(self.data, 'data')
        self.validate_required(self.object_string, 'object_string')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['ErrMessage'] = self.err_message
        result['Data'] = self.data
        result['ObjectString'] = self.object_string
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.err_message = map.get('ErrMessage')
        self.data = map.get('Data')
        self.object_string = map.get('ObjectString')
        return self


class GetSceneDataRequest(TeaModel):
    def __init__(self, token=None):
        self.token = token              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['Token'] = self.token
        return result

    def from_map(self, map={}):
        self.token = map.get('Token')
        return self


class GetSceneDataResponse(TeaModel):
    def __init__(self, request_id=None, success=None, err_message=None, data=None, object_string=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.err_message = err_message  # type: str
        self.data = data                # type: Dict[str, Any]
        self.object_string = object_string  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.err_message, 'err_message')
        self.validate_required(self.data, 'data')
        self.validate_required(self.object_string, 'object_string')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['ErrMessage'] = self.err_message
        result['Data'] = self.data
        result['ObjectString'] = self.object_string
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.err_message = map.get('ErrMessage')
        self.data = map.get('Data')
        self.object_string = map.get('ObjectString')
        return self


class CheckPermissionRequest(TeaModel):
    def __init__(self, aliyun_id=None):
        self.aliyun_id = aliyun_id      # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['AliyunId'] = self.aliyun_id
        return result

    def from_map(self, map={}):
        self.aliyun_id = map.get('AliyunId')
        return self


class CheckPermissionResponse(TeaModel):
    def __init__(self, request_id=None, success=None, err_message=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.err_message = err_message  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.err_message, 'err_message')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['ErrMessage'] = self.err_message
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.err_message = map.get('ErrMessage')
        return self


class CheckResourceRequest(TeaModel):
    def __init__(self, country=None, interrupt=None, invoker=None, pk=None, bid=None, hid=None, task_identifier=None,
                 task_extra_data=None, gmt_wakeup=None, success=None, message=None, level=None, url=None, prompt=None):
        self.country = country          # type: str
        self.interrupt = interrupt      # type: bool
        self.invoker = invoker          # type: str
        self.pk = pk                    # type: str
        self.bid = bid                  # type: str
        self.hid = hid                  # type: int
        self.task_identifier = task_identifier  # type: str
        self.task_extra_data = task_extra_data  # type: str
        self.gmt_wakeup = gmt_wakeup    # type: str
        self.success = success          # type: bool
        self.message = message          # type: str
        self.level = level              # type: int
        self.url = url                  # type: str
        self.prompt = prompt            # type: str

    def validate(self):
        self.validate_required(self.country, 'country')
        self.validate_required(self.invoker, 'invoker')
        self.validate_required(self.pk, 'pk')
        self.validate_required(self.bid, 'bid')
        self.validate_required(self.hid, 'hid')
        self.validate_required(self.task_identifier, 'task_identifier')
        self.validate_required(self.task_extra_data, 'task_extra_data')
        self.validate_required(self.gmt_wakeup, 'gmt_wakeup')

    def to_map(self):
        result = {}
        result['Country'] = self.country
        result['Interrupt'] = self.interrupt
        result['Invoker'] = self.invoker
        result['Pk'] = self.pk
        result['Bid'] = self.bid
        result['Hid'] = self.hid
        result['TaskIdentifier'] = self.task_identifier
        result['TaskExtraData'] = self.task_extra_data
        result['GmtWakeup'] = self.gmt_wakeup
        result['Success'] = self.success
        result['Message'] = self.message
        result['Level'] = self.level
        result['Url'] = self.url
        result['Prompt'] = self.prompt
        return result

    def from_map(self, map={}):
        self.country = map.get('Country')
        self.interrupt = map.get('Interrupt')
        self.invoker = map.get('Invoker')
        self.pk = map.get('Pk')
        self.bid = map.get('Bid')
        self.hid = map.get('Hid')
        self.task_identifier = map.get('TaskIdentifier')
        self.task_extra_data = map.get('TaskExtraData')
        self.gmt_wakeup = map.get('GmtWakeup')
        self.success = map.get('Success')
        self.message = map.get('Message')
        self.level = map.get('Level')
        self.url = map.get('Url')
        self.prompt = map.get('Prompt')
        return self


class CheckResourceResponse(TeaModel):
    def __init__(self, interrupt=None, invoker=None, pk=None, bid=None, hid=None, country=None, task_identifier=None,
                 task_extra_data=None, gmt_wakeup=None, success=None, message=None, level=None, url=None, prompt=None,
                 request_id=None):
        self.interrupt = interrupt      # type: bool
        self.invoker = invoker          # type: str
        self.pk = pk                    # type: str
        self.bid = bid                  # type: str
        self.hid = hid                  # type: int
        self.country = country          # type: str
        self.task_identifier = task_identifier  # type: str
        self.task_extra_data = task_extra_data  # type: str
        self.gmt_wakeup = gmt_wakeup    # type: str
        self.success = success          # type: bool
        self.message = message          # type: str
        self.level = level              # type: int
        self.url = url                  # type: str
        self.prompt = prompt            # type: str
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.interrupt, 'interrupt')
        self.validate_required(self.invoker, 'invoker')
        self.validate_required(self.pk, 'pk')
        self.validate_required(self.bid, 'bid')
        self.validate_required(self.hid, 'hid')
        self.validate_required(self.country, 'country')
        self.validate_required(self.task_identifier, 'task_identifier')
        self.validate_required(self.task_extra_data, 'task_extra_data')
        self.validate_required(self.gmt_wakeup, 'gmt_wakeup')
        self.validate_required(self.success, 'success')
        self.validate_required(self.message, 'message')
        self.validate_required(self.level, 'level')
        self.validate_required(self.url, 'url')
        self.validate_required(self.prompt, 'prompt')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['Interrupt'] = self.interrupt
        result['Invoker'] = self.invoker
        result['Pk'] = self.pk
        result['Bid'] = self.bid
        result['Hid'] = self.hid
        result['Country'] = self.country
        result['TaskIdentifier'] = self.task_identifier
        result['TaskExtraData'] = self.task_extra_data
        result['GmtWakeup'] = self.gmt_wakeup
        result['Success'] = self.success
        result['Message'] = self.message
        result['Level'] = self.level
        result['Url'] = self.url
        result['Prompt'] = self.prompt
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.interrupt = map.get('Interrupt')
        self.invoker = map.get('Invoker')
        self.pk = map.get('Pk')
        self.bid = map.get('Bid')
        self.hid = map.get('Hid')
        self.country = map.get('Country')
        self.task_identifier = map.get('TaskIdentifier')
        self.task_extra_data = map.get('TaskExtraData')
        self.gmt_wakeup = map.get('GmtWakeup')
        self.success = map.get('Success')
        self.message = map.get('Message')
        self.level = map.get('Level')
        self.url = map.get('Url')
        self.prompt = map.get('Prompt')
        self.request_id = map.get('RequestId')
        return self


class CreateSceneRequest(TeaModel):
    def __init__(self, name=None, project_id=None):
        self.name = name                # type: str
        self.project_id = project_id    # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['ProjectId'] = self.project_id
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.project_id = map.get('ProjectId')
        return self


class CreateSceneResponse(TeaModel):
    def __init__(self, request_id=None, scene_id=None, success=None, err_message=None, preview_token=None):
        self.request_id = request_id    # type: str
        self.scene_id = scene_id        # type: int
        self.success = success          # type: bool
        self.err_message = err_message  # type: str
        self.preview_token = preview_token  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.scene_id, 'scene_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.err_message, 'err_message')
        self.validate_required(self.preview_token, 'preview_token')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['SceneId'] = self.scene_id
        result['Success'] = self.success
        result['ErrMessage'] = self.err_message
        result['PreviewToken'] = self.preview_token
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.scene_id = map.get('SceneId')
        self.success = map.get('Success')
        self.err_message = map.get('ErrMessage')
        self.preview_token = map.get('PreviewToken')
        return self


class CreateProjectRequest(TeaModel):
    def __init__(self, name=None, business_id=None, business_user_id_list=None, gather_user_id_list=None,
                 builder_user_id_list=None):
        self.name = name                # type: str
        self.business_id = business_id  # type: str
        self.business_user_id_list = business_user_id_list  # type: str
        self.gather_user_id_list = gather_user_id_list  # type: str
        self.builder_user_id_list = builder_user_id_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['BusinessId'] = self.business_id
        result['BusinessUserIdList'] = self.business_user_id_list
        result['GatherUserIdList'] = self.gather_user_id_list
        result['BuilderUserIdList'] = self.builder_user_id_list
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.business_id = map.get('BusinessId')
        self.business_user_id_list = map.get('BusinessUserIdList')
        self.gather_user_id_list = map.get('GatherUserIdList')
        self.builder_user_id_list = map.get('BuilderUserIdList')
        return self


class CreateProjectResponse(TeaModel):
    def __init__(self, request_id=None, id=None, name=None, success=None, err_message=None):
        self.request_id = request_id    # type: str
        self.id = id                    # type: int
        self.name = name                # type: str
        self.success = success          # type: bool
        self.err_message = err_message  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.id, 'id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.success, 'success')
        self.validate_required(self.err_message, 'err_message')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Id'] = self.id
        result['Name'] = self.name
        result['Success'] = self.success
        result['ErrMessage'] = self.err_message
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.id = map.get('Id')
        self.name = map.get('Name')
        self.success = map.get('Success')
        self.err_message = map.get('ErrMessage')
        return self


class DeleteProjectRequest(TeaModel):
    def __init__(self, project_id=None):
        self.project_id = project_id    # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        return self


class DeleteProjectResponse(TeaModel):
    def __init__(self, request_id=None, success=None, err_message=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.err_message = err_message  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.err_message, 'err_message')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['ErrMessage'] = self.err_message
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.err_message = map.get('ErrMessage')
        return self


class ListScenesRequest(TeaModel):
    def __init__(self, project_id=None, is_publish_query=None):
        self.project_id = project_id    # type: str
        self.is_publish_query = is_publish_query  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        result['IsPublishQuery'] = self.is_publish_query
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        self.is_publish_query = map.get('IsPublishQuery')
        return self


class ListScenesResponse(TeaModel):
    def __init__(self, request_id=None, success=None, err_message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.err_message = err_message  # type: str
        self.data = data                # type: List[ListScenesResponseData]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.err_message, 'err_message')
        self.validate_required(self.data, 'data')
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['ErrMessage'] = self.err_message
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.err_message = map.get('ErrMessage')
        self.data = []
        if map.get('Data') is not None:
            for k in map.get('Data'):
                temp_model = ListScenesResponseData()
                self.data.append(temp_model.from_map(k))
        else:
            self.data = None
        return self


class ListScenesResponseData(TeaModel):
    def __init__(self, scene_id=None):
        self.scene_id = scene_id        # type: str

    def validate(self):
        self.validate_required(self.scene_id, 'scene_id')

    def to_map(self):
        result = {}
        result['SceneId'] = self.scene_id
        return result

    def from_map(self, map={}):
        self.scene_id = map.get('SceneId')
        return self


