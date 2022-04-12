# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AdaptCreateServiceRequestAdaptTarget(TeaModel):
    def __init__(
        self,
        bit_rate: int = None,
        frame_rate: int = None,
        resolution: str = None,
        start_program: str = None,
    ):
        self.bit_rate = bit_rate
        self.frame_rate = frame_rate
        self.resolution = resolution
        self.start_program = start_program

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bit_rate is not None:
            result['BitRate'] = self.bit_rate
        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        if self.start_program is not None:
            result['StartProgram'] = self.start_program
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BitRate') is not None:
            self.bit_rate = m.get('BitRate')
        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        if m.get('StartProgram') is not None:
            self.start_program = m.get('StartProgram')
        return self


class AdaptCreateServiceRequest(TeaModel):
    def __init__(
        self,
        adapt_target: AdaptCreateServiceRequestAdaptTarget = None,
        app_version_id: str = None,
        app_version_name: str = None,
        request_app: str = None,
    ):
        self.adapt_target = adapt_target
        self.app_version_id = app_version_id
        self.app_version_name = app_version_name
        self.request_app = request_app

    def validate(self):
        if self.adapt_target:
            self.adapt_target.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adapt_target is not None:
            result['AdaptTarget'] = self.adapt_target.to_map()
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        if self.app_version_name is not None:
            result['AppVersionName'] = self.app_version_name
        if self.request_app is not None:
            result['RequestApp'] = self.request_app
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdaptTarget') is not None:
            temp_model = AdaptCreateServiceRequestAdaptTarget()
            self.adapt_target = temp_model.from_map(m['AdaptTarget'])
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        if m.get('AppVersionName') is not None:
            self.app_version_name = m.get('AppVersionName')
        if m.get('RequestApp') is not None:
            self.request_app = m.get('RequestApp')
        return self


class AdaptCreateServiceShrinkRequest(TeaModel):
    def __init__(
        self,
        adapt_target_shrink: str = None,
        app_version_id: str = None,
        app_version_name: str = None,
        request_app: str = None,
    ):
        self.adapt_target_shrink = adapt_target_shrink
        self.app_version_id = app_version_id
        self.app_version_name = app_version_name
        self.request_app = request_app

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adapt_target_shrink is not None:
            result['AdaptTarget'] = self.adapt_target_shrink
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        if self.app_version_name is not None:
            result['AppVersionName'] = self.app_version_name
        if self.request_app is not None:
            result['RequestApp'] = self.request_app
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdaptTarget') is not None:
            self.adapt_target_shrink = m.get('AdaptTarget')
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        if m.get('AppVersionName') is not None:
            self.app_version_name = m.get('AppVersionName')
        if m.get('RequestApp') is not None:
            self.request_app = m.get('RequestApp')
        return self


class AdaptCreateServiceResponseBodyData(TeaModel):
    def __init__(
        self,
        adapt_apply_id: int = None,
    ):
        self.adapt_apply_id = adapt_apply_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adapt_apply_id is not None:
            result['AdaptApplyId'] = self.adapt_apply_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdaptApplyId') is not None:
            self.adapt_apply_id = m.get('AdaptApplyId')
        return self


class AdaptCreateServiceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: AdaptCreateServiceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AdaptCreateServiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AdaptCreateServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AdaptCreateServiceResponseBody = None,
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
            temp_model = AdaptCreateServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AdaptGetServiceRequest(TeaModel):
    def __init__(
        self,
        app_version_id: str = None,
        request_app: str = None,
    ):
        self.app_version_id = app_version_id
        self.request_app = request_app

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        if self.request_app is not None:
            result['RequestApp'] = self.request_app
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        if m.get('RequestApp') is not None:
            self.request_app = m.get('RequestApp')
        return self


class AdaptGetServiceResponseBodyDataAdaptTarget(TeaModel):
    def __init__(
        self,
        bit_rate: int = None,
        frame_rate: int = None,
        resolution: str = None,
        start_program: str = None,
    ):
        self.bit_rate = bit_rate
        self.frame_rate = frame_rate
        self.resolution = resolution
        self.start_program = start_program

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bit_rate is not None:
            result['BitRate'] = self.bit_rate
        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        if self.start_program is not None:
            result['StartProgram'] = self.start_program
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BitRate') is not None:
            self.bit_rate = m.get('BitRate')
        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        if m.get('StartProgram') is not None:
            self.start_program = m.get('StartProgram')
        return self


class AdaptGetServiceResponseBodyData(TeaModel):
    def __init__(
        self,
        adapt_status: str = None,
        adapt_target: AdaptGetServiceResponseBodyDataAdaptTarget = None,
        app_id: str = None,
        app_version_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        tenant_id: int = None,
    ):
        self.adapt_status = adapt_status
        self.adapt_target = adapt_target
        self.app_id = app_id
        self.app_version_id = app_version_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.tenant_id = tenant_id

    def validate(self):
        if self.adapt_target:
            self.adapt_target.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adapt_status is not None:
            result['AdaptStatus'] = self.adapt_status
        if self.adapt_target is not None:
            result['AdaptTarget'] = self.adapt_target.to_map()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdaptStatus') is not None:
            self.adapt_status = m.get('AdaptStatus')
        if m.get('AdaptTarget') is not None:
            temp_model = AdaptGetServiceResponseBodyDataAdaptTarget()
            self.adapt_target = temp_model.from_map(m['AdaptTarget'])
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class AdaptGetServiceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: AdaptGetServiceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AdaptGetServiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AdaptGetServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AdaptGetServiceResponseBody = None,
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
            temp_model = AdaptGetServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AppCreateServiceRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_type: str = None,
        request_app: str = None,
    ):
        self.app_name = app_name
        self.app_type = app_type
        self.request_app = request_app

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.request_app is not None:
            result['RequestApp'] = self.request_app
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('RequestApp') is not None:
            self.request_app = m.get('RequestApp')
        return self


class AppCreateServiceResponseBodyData(TeaModel):
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


class AppCreateServiceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: AppCreateServiceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AppCreateServiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AppCreateServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AppCreateServiceResponseBody = None,
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
            temp_model = AppCreateServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AppDeleteServiceRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_app: str = None,
    ):
        self.app_id = app_id
        self.request_app = request_app

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_app is not None:
            result['RequestApp'] = self.request_app
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestApp') is not None:
            self.request_app = m.get('RequestApp')
        return self


class AppDeleteServiceResponseBodyData(TeaModel):
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


class AppDeleteServiceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: AppDeleteServiceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AppDeleteServiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AppDeleteServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AppDeleteServiceResponseBody = None,
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
            temp_model = AppDeleteServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AppGetServiceRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_app: str = None,
    ):
        self.app_id = app_id
        self.request_app = request_app

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_app is not None:
            result['RequestApp'] = self.request_app
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestApp') is not None:
            self.request_app = m.get('RequestApp')
        return self


class AppGetServiceResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        app_type: str = None,
        biz_type: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        tenant_id: int = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.app_type = app_type
        self.biz_type = biz_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class AppGetServiceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: AppGetServiceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AppGetServiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AppGetServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AppGetServiceResponseBody = None,
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
            temp_model = AppGetServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AppListServiceRequest(TeaModel):
    def __init__(
        self,
        key_search: str = None,
        page_number: int = None,
        page_size: int = None,
        request_app: str = None,
    ):
        self.key_search = key_search
        self.page_number = page_number
        self.page_size = page_size
        self.request_app = request_app

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_search is not None:
            result['KeySearch'] = self.key_search
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_app is not None:
            result['RequestApp'] = self.request_app
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeySearch') is not None:
            self.key_search = m.get('KeySearch')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestApp') is not None:
            self.request_app = m.get('RequestApp')
        return self


class AppListServiceResponseBodyDataApps(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        app_type: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        tenant_id: int = None,
        version_adapt_num: int = None,
        version_total_num: int = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.app_type = app_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.tenant_id = tenant_id
        self.version_adapt_num = version_adapt_num
        self.version_total_num = version_total_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.version_adapt_num is not None:
            result['VersionAdaptNum'] = self.version_adapt_num
        if self.version_total_num is not None:
            result['VersionTotalNum'] = self.version_total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('VersionAdaptNum') is not None:
            self.version_adapt_num = m.get('VersionAdaptNum')
        if m.get('VersionTotalNum') is not None:
            self.version_total_num = m.get('VersionTotalNum')
        return self


class AppListServiceResponseBodyData(TeaModel):
    def __init__(
        self,
        apps: List[AppListServiceResponseBodyDataApps] = None,
        total: int = None,
    ):
        self.apps = apps
        self.total = total

    def validate(self):
        if self.apps:
            for k in self.apps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Apps'] = []
        if self.apps is not None:
            for k in self.apps:
                result['Apps'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.apps = []
        if m.get('Apps') is not None:
            for k in m.get('Apps'):
                temp_model = AppListServiceResponseBodyDataApps()
                self.apps.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class AppListServiceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: AppListServiceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AppListServiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AppListServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AppListServiceResponseBody = None,
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
            temp_model = AppListServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AppModifyServiceRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        request_app: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.request_app = request_app

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.request_app is not None:
            result['RequestApp'] = self.request_app
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('RequestApp') is not None:
            self.request_app = m.get('RequestApp')
        return self


class AppModifyServiceResponseBodyData(TeaModel):
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


class AppModifyServiceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: AppModifyServiceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AppModifyServiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AppModifyServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AppModifyServiceResponseBody = None,
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
            temp_model = AppModifyServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AppVersionCreateServiceRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_version_name: str = None,
        file_address: str = None,
        file_size: int = None,
        file_upload_type: str = None,
        request_app: str = None,
    ):
        self.app_id = app_id
        self.app_version_name = app_version_name
        self.file_address = file_address
        self.file_size = file_size
        self.file_upload_type = file_upload_type
        self.request_app = request_app

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version_name is not None:
            result['AppVersionName'] = self.app_version_name
        if self.file_address is not None:
            result['FileAddress'] = self.file_address
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_upload_type is not None:
            result['FileUploadType'] = self.file_upload_type
        if self.request_app is not None:
            result['RequestApp'] = self.request_app
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersionName') is not None:
            self.app_version_name = m.get('AppVersionName')
        if m.get('FileAddress') is not None:
            self.file_address = m.get('FileAddress')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileUploadType') is not None:
            self.file_upload_type = m.get('FileUploadType')
        if m.get('RequestApp') is not None:
            self.request_app = m.get('RequestApp')
        return self


class AppVersionCreateServiceResponseBodyData(TeaModel):
    def __init__(
        self,
        app_version_id: str = None,
    ):
        self.app_version_id = app_version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        return self


class AppVersionCreateServiceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: AppVersionCreateServiceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AppVersionCreateServiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AppVersionCreateServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AppVersionCreateServiceResponseBody = None,
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
            temp_model = AppVersionCreateServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AppVersionDeleteServiceRequest(TeaModel):
    def __init__(
        self,
        app_version_id: str = None,
        request_app: str = None,
    ):
        self.app_version_id = app_version_id
        self.request_app = request_app

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        if self.request_app is not None:
            result['RequestApp'] = self.request_app
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        if m.get('RequestApp') is not None:
            self.request_app = m.get('RequestApp')
        return self


class AppVersionDeleteServiceResponseBodyData(TeaModel):
    def __init__(
        self,
        app_version_id: str = None,
    ):
        self.app_version_id = app_version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        return self


class AppVersionDeleteServiceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: AppVersionDeleteServiceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AppVersionDeleteServiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AppVersionDeleteServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AppVersionDeleteServiceResponseBody = None,
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
            temp_model = AppVersionDeleteServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AppVersionGetServiceRequest(TeaModel):
    def __init__(
        self,
        app_version_id: str = None,
        request_app: str = None,
    ):
        self.app_version_id = app_version_id
        self.request_app = request_app

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        if self.request_app is not None:
            result['RequestApp'] = self.request_app
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        if m.get('RequestApp') is not None:
            self.request_app = m.get('RequestApp')
        return self


class AppVersionGetServiceResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_version_id: str = None,
        app_version_name: str = None,
        app_version_status: str = None,
        app_version_status_memo: str = None,
        consume_cu: float = None,
        file_address: str = None,
        file_size: int = None,
        file_upload_finish_time: str = None,
        file_upload_type: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        source_version_id: str = None,
        tenant_id: int = None,
    ):
        self.app_id = app_id
        self.app_version_id = app_version_id
        self.app_version_name = app_version_name
        self.app_version_status = app_version_status
        self.app_version_status_memo = app_version_status_memo
        self.consume_cu = consume_cu
        self.file_address = file_address
        self.file_size = file_size
        self.file_upload_finish_time = file_upload_finish_time
        self.file_upload_type = file_upload_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.source_version_id = source_version_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        if self.app_version_name is not None:
            result['AppVersionName'] = self.app_version_name
        if self.app_version_status is not None:
            result['AppVersionStatus'] = self.app_version_status
        if self.app_version_status_memo is not None:
            result['AppVersionStatusMemo'] = self.app_version_status_memo
        if self.consume_cu is not None:
            result['ConsumeCu'] = self.consume_cu
        if self.file_address is not None:
            result['FileAddress'] = self.file_address
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_upload_finish_time is not None:
            result['FileUploadFinishTime'] = self.file_upload_finish_time
        if self.file_upload_type is not None:
            result['FileUploadType'] = self.file_upload_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.source_version_id is not None:
            result['SourceVersionId'] = self.source_version_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        if m.get('AppVersionName') is not None:
            self.app_version_name = m.get('AppVersionName')
        if m.get('AppVersionStatus') is not None:
            self.app_version_status = m.get('AppVersionStatus')
        if m.get('AppVersionStatusMemo') is not None:
            self.app_version_status_memo = m.get('AppVersionStatusMemo')
        if m.get('ConsumeCu') is not None:
            self.consume_cu = m.get('ConsumeCu')
        if m.get('FileAddress') is not None:
            self.file_address = m.get('FileAddress')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileUploadFinishTime') is not None:
            self.file_upload_finish_time = m.get('FileUploadFinishTime')
        if m.get('FileUploadType') is not None:
            self.file_upload_type = m.get('FileUploadType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('SourceVersionId') is not None:
            self.source_version_id = m.get('SourceVersionId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class AppVersionGetServiceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: AppVersionGetServiceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AppVersionGetServiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AppVersionGetServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AppVersionGetServiceResponseBody = None,
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
            temp_model = AppVersionGetServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AppVersionListServiceRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        page_number: int = None,
        page_size: int = None,
        request_app: str = None,
    ):
        self.app_id = app_id
        self.page_number = page_number
        self.page_size = page_size
        self.request_app = request_app

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_app is not None:
            result['RequestApp'] = self.request_app
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestApp') is not None:
            self.request_app = m.get('RequestApp')
        return self


class AppVersionListServiceResponseBodyDataVersions(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_version_id: str = None,
        app_version_name: str = None,
        app_version_status: str = None,
        app_version_status_memo: str = None,
        consume_cu: float = None,
        file_address: str = None,
        file_size: int = None,
        file_upload_finish_time: str = None,
        file_upload_type: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        tenant_id: int = None,
    ):
        self.app_id = app_id
        self.app_version_id = app_version_id
        self.app_version_name = app_version_name
        self.app_version_status = app_version_status
        self.app_version_status_memo = app_version_status_memo
        self.consume_cu = consume_cu
        self.file_address = file_address
        self.file_size = file_size
        self.file_upload_finish_time = file_upload_finish_time
        self.file_upload_type = file_upload_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        if self.app_version_name is not None:
            result['AppVersionName'] = self.app_version_name
        if self.app_version_status is not None:
            result['AppVersionStatus'] = self.app_version_status
        if self.app_version_status_memo is not None:
            result['AppVersionStatusMemo'] = self.app_version_status_memo
        if self.consume_cu is not None:
            result['ConsumeCu'] = self.consume_cu
        if self.file_address is not None:
            result['FileAddress'] = self.file_address
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_upload_finish_time is not None:
            result['FileUploadFinishTime'] = self.file_upload_finish_time
        if self.file_upload_type is not None:
            result['FileUploadType'] = self.file_upload_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        if m.get('AppVersionName') is not None:
            self.app_version_name = m.get('AppVersionName')
        if m.get('AppVersionStatus') is not None:
            self.app_version_status = m.get('AppVersionStatus')
        if m.get('AppVersionStatusMemo') is not None:
            self.app_version_status_memo = m.get('AppVersionStatusMemo')
        if m.get('ConsumeCu') is not None:
            self.consume_cu = m.get('ConsumeCu')
        if m.get('FileAddress') is not None:
            self.file_address = m.get('FileAddress')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileUploadFinishTime') is not None:
            self.file_upload_finish_time = m.get('FileUploadFinishTime')
        if m.get('FileUploadType') is not None:
            self.file_upload_type = m.get('FileUploadType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class AppVersionListServiceResponseBodyData(TeaModel):
    def __init__(
        self,
        total: int = None,
        versions: List[AppVersionListServiceResponseBodyDataVersions] = None,
    ):
        self.total = total
        self.versions = versions

    def validate(self):
        if self.versions:
            for k in self.versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total is not None:
            result['Total'] = self.total
        result['Versions'] = []
        if self.versions is not None:
            for k in self.versions:
                result['Versions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.versions = []
        if m.get('Versions') is not None:
            for k in m.get('Versions'):
                temp_model = AppVersionListServiceResponseBodyDataVersions()
                self.versions.append(temp_model.from_map(k))
        return self


class AppVersionListServiceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: AppVersionListServiceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AppVersionListServiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AppVersionListServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AppVersionListServiceResponseBody = None,
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
            temp_model = AppVersionListServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AppVersionModifyServiceRequest(TeaModel):
    def __init__(
        self,
        app_version_id: str = None,
        app_version_name: str = None,
        request_app: str = None,
    ):
        self.app_version_id = app_version_id
        self.app_version_name = app_version_name
        self.request_app = request_app

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        if self.app_version_name is not None:
            result['AppVersionName'] = self.app_version_name
        if self.request_app is not None:
            result['RequestApp'] = self.request_app
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        if m.get('AppVersionName') is not None:
            self.app_version_name = m.get('AppVersionName')
        if m.get('RequestApp') is not None:
            self.request_app = m.get('RequestApp')
        return self


class AppVersionModifyServiceResponseBodyData(TeaModel):
    def __init__(
        self,
        app_version_id: str = None,
    ):
        self.app_version_id = app_version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        return self


class AppVersionModifyServiceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: AppVersionModifyServiceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AppVersionModifyServiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AppVersionModifyServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AppVersionModifyServiceResponseBody = None,
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
            temp_model = AppVersionModifyServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AppVersionQueryServiceRequest(TeaModel):
    def __init__(
        self,
        key_search: str = None,
        page_number: int = None,
        page_size: int = None,
        request_app: str = None,
    ):
        self.key_search = key_search
        self.page_number = page_number
        self.page_size = page_size
        self.request_app = request_app

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_search is not None:
            result['KeySearch'] = self.key_search
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_app is not None:
            result['RequestApp'] = self.request_app
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeySearch') is not None:
            self.key_search = m.get('KeySearch')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestApp') is not None:
            self.request_app = m.get('RequestApp')
        return self


class AppVersionQueryServiceResponseBodyDataVersions(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        app_version_id: str = None,
        app_version_name: str = None,
        tenant_id: int = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.app_version_id = app_version_id
        self.app_version_name = app_version_name
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        if self.app_version_name is not None:
            result['AppVersionName'] = self.app_version_name
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        if m.get('AppVersionName') is not None:
            self.app_version_name = m.get('AppVersionName')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class AppVersionQueryServiceResponseBodyData(TeaModel):
    def __init__(
        self,
        total: int = None,
        versions: List[AppVersionQueryServiceResponseBodyDataVersions] = None,
    ):
        self.total = total
        self.versions = versions

    def validate(self):
        if self.versions:
            for k in self.versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total is not None:
            result['Total'] = self.total
        result['Versions'] = []
        if self.versions is not None:
            for k in self.versions:
                result['Versions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.versions = []
        if m.get('Versions') is not None:
            for k in m.get('Versions'):
                temp_model = AppVersionQueryServiceResponseBodyDataVersions()
                self.versions.append(temp_model.from_map(k))
        return self


class AppVersionQueryServiceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: AppVersionQueryServiceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AppVersionQueryServiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AppVersionQueryServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AppVersionQueryServiceResponseBody = None,
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
            temp_model = AppVersionQueryServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AppliedConsumStatRequest(TeaModel):
    def __init__(
        self,
        applied_id: List[str] = None,
        operator_id: str = None,
        operator_type: str = None,
        package_type: str = None,
        query_end_date: str = None,
        query_start_date: str = None,
    ):
        self.applied_id = applied_id
        # 请求操作人Id
        self.operator_id = operator_id
        # 请求操作人类型
        self.operator_type = operator_type
        # 资源类型,PackageType[CU(cu),code,cssResourceType,desc]
        self.package_type = package_type
        # 查询结束时间
        self.query_end_date = query_end_date
        # 查询开始时间
        self.query_start_date = query_start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applied_id is not None:
            result['AppliedId'] = self.applied_id
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.query_end_date is not None:
            result['QueryEndDate'] = self.query_end_date
        if self.query_start_date is not None:
            result['QueryStartDate'] = self.query_start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppliedId') is not None:
            self.applied_id = m.get('AppliedId')
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('QueryEndDate') is not None:
            self.query_end_date = m.get('QueryEndDate')
        if m.get('QueryStartDate') is not None:
            self.query_start_date = m.get('QueryStartDate')
        return self


class AppliedConsumStatShrinkRequest(TeaModel):
    def __init__(
        self,
        applied_id_shrink: str = None,
        operator_id: str = None,
        operator_type: str = None,
        package_type: str = None,
        query_end_date: str = None,
        query_start_date: str = None,
    ):
        self.applied_id_shrink = applied_id_shrink
        # 请求操作人Id
        self.operator_id = operator_id
        # 请求操作人类型
        self.operator_type = operator_type
        # 资源类型,PackageType[CU(cu),code,cssResourceType,desc]
        self.package_type = package_type
        # 查询结束时间
        self.query_end_date = query_end_date
        # 查询开始时间
        self.query_start_date = query_start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applied_id_shrink is not None:
            result['AppliedId'] = self.applied_id_shrink
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.query_end_date is not None:
            result['QueryEndDate'] = self.query_end_date
        if self.query_start_date is not None:
            result['QueryStartDate'] = self.query_start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppliedId') is not None:
            self.applied_id_shrink = m.get('AppliedId')
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('QueryEndDate') is not None:
            self.query_end_date = m.get('QueryEndDate')
        if m.get('QueryStartDate') is not None:
            self.query_start_date = m.get('QueryStartDate')
        return self


class DataAppliedConsumptionMapValue(TeaModel):
    def __init__(
        self,
        applied_id: str = None,
        stat_date: str = None,
        consumption_cu: int = None,
    ):
        # 应用ID
        self.applied_id = applied_id
        # 统计日期
        self.stat_date = stat_date
        # 分钟级消耗CU
        self.consumption_cu = consumption_cu

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applied_id is not None:
            result['AppliedId'] = self.applied_id
        if self.stat_date is not None:
            result['StatDate'] = self.stat_date
        if self.consumption_cu is not None:
            result['ConsumptionCu'] = self.consumption_cu
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppliedId') is not None:
            self.applied_id = m.get('AppliedId')
        if m.get('StatDate') is not None:
            self.stat_date = m.get('StatDate')
        if m.get('ConsumptionCu') is not None:
            self.consumption_cu = m.get('ConsumptionCu')
        return self


class AppliedConsumStatResponseBodyData(TeaModel):
    def __init__(
        self,
        applied_consumption_map: Dict[str, List[DataAppliedConsumptionMapValue]] = None,
    ):
        # 应用消耗Cu统计
        self.applied_consumption_map = applied_consumption_map

    def validate(self):
        if self.applied_consumption_map:
            for v in self.applied_consumption_map.values():
                for k1 in v:
                    if k1:
                        k1.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppliedConsumptionMap'] = {}
        if self.applied_consumption_map is not None:
            for k, v in self.applied_consumption_map.items():
                l1 = []
                for k1 in v:
                    l1.append(k1.to_map() if k1 else None)
                result['appliedConsumptionMap'][k] = l1
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.applied_consumption_map = {}
        if m.get('AppliedConsumptionMap') is not None:
            for k, v in m.get('AppliedConsumptionMap').items():
                l1 = []
                for k1 in v:
                    temp_model = DataAppliedConsumptionMapValue()
                    l1.append(temp_model.from_map(k1))
                self.applied_consumption_map['k'] = l1
        return self


class AppliedConsumStatResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: AppliedConsumStatResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 业务处理结果Code
        self.code = code
        # 业务对象
        self.data = data
        # 业务处理消息摘要
        self.message = message
        # 操作请求ID
        self.request_id = request_id
        # 业务处理是否成功
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
            temp_model = AppliedConsumStatResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AppliedConsumStatResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AppliedConsumStatResponseBody = None,
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
            temp_model = AppliedConsumStatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AppliedNearRealStatRequest(TeaModel):
    def __init__(
        self,
        applied_version_id: List[str] = None,
        operator_id: str = None,
        operator_type: str = None,
        order_by: str = None,
        package_type: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.applied_version_id = applied_version_id
        # 请求操作人Id
        self.operator_id = operator_id
        # 请求操作人类型
        self.operator_type = operator_type
        # 排序类型。默认：AppliedConcurrency_Desc,AppliedNearRealOrderConditionType[AppliedConcurrency_Desc(AppliedConcurrency_Desc,根据实时并发路数降序排列),AppliedConcurrency_Asc(AppliedConcurrency_Asc,根据实时并发路数升序排列),AppliedConsumptionCu_Desc(AppliedConsumptionCu_Desc,根据实时CU消耗降序排列),AppliedConsumptionCu_Asc(AppliedConsumptionCu_Asc,根据实时CU消耗升序排列),orderByType,desc]
        self.order_by = order_by
        # 资源类型,PackageType[CU(cu),code,cssResourceType,desc]
        self.package_type = package_type
        # 当前页码，默认1
        self.page_number = page_number
        # 每页项数，默认20,最大100
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applied_version_id is not None:
            result['AppliedVersionId'] = self.applied_version_id
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppliedVersionId') is not None:
            self.applied_version_id = m.get('AppliedVersionId')
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class AppliedNearRealStatShrinkRequest(TeaModel):
    def __init__(
        self,
        applied_version_id_shrink: str = None,
        operator_id: str = None,
        operator_type: str = None,
        order_by: str = None,
        package_type: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.applied_version_id_shrink = applied_version_id_shrink
        # 请求操作人Id
        self.operator_id = operator_id
        # 请求操作人类型
        self.operator_type = operator_type
        # 排序类型。默认：AppliedConcurrency_Desc,AppliedNearRealOrderConditionType[AppliedConcurrency_Desc(AppliedConcurrency_Desc,根据实时并发路数降序排列),AppliedConcurrency_Asc(AppliedConcurrency_Asc,根据实时并发路数升序排列),AppliedConsumptionCu_Desc(AppliedConsumptionCu_Desc,根据实时CU消耗降序排列),AppliedConsumptionCu_Asc(AppliedConsumptionCu_Asc,根据实时CU消耗升序排列),orderByType,desc]
        self.order_by = order_by
        # 资源类型,PackageType[CU(cu),code,cssResourceType,desc]
        self.package_type = package_type
        # 当前页码，默认1
        self.page_number = page_number
        # 每页项数，默认20,最大100
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applied_version_id_shrink is not None:
            result['AppliedVersionId'] = self.applied_version_id_shrink
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppliedVersionId') is not None:
            self.applied_version_id_shrink = m.get('AppliedVersionId')
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class AppliedNearRealStatResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        applied_id: str = None,
        applied_name: str = None,
        applied_version_id: str = None,
        applied_version_name: str = None,
        concurrency: int = None,
        consumption_cu: float = None,
    ):
        # 应用ID
        self.applied_id = applied_id
        # 应用名称
        self.applied_name = applied_name
        # 应用版本ID
        self.applied_version_id = applied_version_id
        # 应用版本名称
        self.applied_version_name = applied_version_name
        # 实时消耗并发
        self.concurrency = concurrency
        # 实时消耗CU
        self.consumption_cu = consumption_cu

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applied_id is not None:
            result['AppliedId'] = self.applied_id
        if self.applied_name is not None:
            result['AppliedName'] = self.applied_name
        if self.applied_version_id is not None:
            result['AppliedVersionId'] = self.applied_version_id
        if self.applied_version_name is not None:
            result['AppliedVersionName'] = self.applied_version_name
        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency
        if self.consumption_cu is not None:
            result['ConsumptionCu'] = self.consumption_cu
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppliedId') is not None:
            self.applied_id = m.get('AppliedId')
        if m.get('AppliedName') is not None:
            self.applied_name = m.get('AppliedName')
        if m.get('AppliedVersionId') is not None:
            self.applied_version_id = m.get('AppliedVersionId')
        if m.get('AppliedVersionName') is not None:
            self.applied_version_name = m.get('AppliedVersionName')
        if m.get('Concurrency') is not None:
            self.concurrency = m.get('Concurrency')
        if m.get('ConsumptionCu') is not None:
            self.consumption_cu = m.get('ConsumptionCu')
        return self


class AppliedNearRealStatResponseBodyData(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        pages: int = None,
        records: List[AppliedNearRealStatResponseBodyDataRecords] = None,
        total_count: int = None,
    ):
        # 当前页码，默认1
        self.page_number = page_number
        # 每页项数，默认20,最大100
        self.page_size = page_size
        # 总页数
        self.pages = pages
        # 结果集
        self.records = records
        # 总共项数
        self.total_count = total_count

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pages is not None:
            result['Pages'] = self.pages
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = AppliedNearRealStatResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class AppliedNearRealStatResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: AppliedNearRealStatResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 业务处理结果Code
        self.code = code
        # 业务对象
        self.data = data
        # 业务处理消息摘要
        self.message = message
        # 操作请求ID
        self.request_id = request_id
        # 业务处理是否成功
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
            temp_model = AppliedNearRealStatResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AppliedNearRealStatResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AppliedNearRealStatResponseBody = None,
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
            temp_model = AppliedNearRealStatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AppliedStatRequest(TeaModel):
    def __init__(
        self,
        operator_id: str = None,
        operator_type: str = None,
        query_end_date: str = None,
        query_start_date: str = None,
    ):
        # 请求操作人Id
        self.operator_id = operator_id
        # 请求操作人类型
        self.operator_type = operator_type
        # 查询结束时间
        self.query_end_date = query_end_date
        # 查询开始时间
        self.query_start_date = query_start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.query_end_date is not None:
            result['QueryEndDate'] = self.query_end_date
        if self.query_start_date is not None:
            result['QueryStartDate'] = self.query_start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('QueryEndDate') is not None:
            self.query_end_date = m.get('QueryEndDate')
        if m.get('QueryStartDate') is not None:
            self.query_start_date = m.get('QueryStartDate')
        return self


class AppliedStatResponseBodyData(TeaModel):
    def __init__(
        self,
        active_applications: int = None,
        average_daily_runtime: int = None,
        peak_concurrency: int = None,
        secondary_average_time: int = None,
    ):
        # 活跃应用个数
        self.active_applications = active_applications
        # 日均应用运行时长
        self.average_daily_runtime = average_daily_runtime
        # 应用并发数量峰值
        self.peak_concurrency = peak_concurrency
        # 次均应用时长
        self.secondary_average_time = secondary_average_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_applications is not None:
            result['ActiveApplications'] = self.active_applications
        if self.average_daily_runtime is not None:
            result['AverageDailyRuntime'] = self.average_daily_runtime
        if self.peak_concurrency is not None:
            result['PeakConcurrency'] = self.peak_concurrency
        if self.secondary_average_time is not None:
            result['SecondaryAverageTime'] = self.secondary_average_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveApplications') is not None:
            self.active_applications = m.get('ActiveApplications')
        if m.get('AverageDailyRuntime') is not None:
            self.average_daily_runtime = m.get('AverageDailyRuntime')
        if m.get('PeakConcurrency') is not None:
            self.peak_concurrency = m.get('PeakConcurrency')
        if m.get('SecondaryAverageTime') is not None:
            self.secondary_average_time = m.get('SecondaryAverageTime')
        return self


class AppliedStatResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: AppliedStatResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 业务处理结果Code
        self.code = code
        # 业务对象
        self.data = data
        # 业务处理消息摘要
        self.message = message
        # 操作请求ID
        self.request_id = request_id
        # 业务处理是否成功
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
            temp_model = AppliedStatResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AppliedStatResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AppliedStatResponseBody = None,
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
            temp_model = AppliedStatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppSessionRequestStartParameters(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # key
        self.key = key
        # value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateAppSessionRequestSystemInfo(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateAppSessionRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_version: str = None,
        client_ip: str = None,
        custom_session_id: str = None,
        custom_user_id: str = None,
        start_parameters: List[CreateAppSessionRequestStartParameters] = None,
        system_info: List[CreateAppSessionRequestSystemInfo] = None,
    ):
        # 应用ID
        self.app_id = app_id
        # 应用版本
        self.app_version = app_version
        # 客户端ip
        self.client_ip = client_ip
        # 自定义会话id
        self.custom_session_id = custom_session_id
        # 自定义用户id
        self.custom_user_id = custom_user_id
        # 启动参数
        self.start_parameters = start_parameters
        # 系统信息：如端侧机型等信息
        self.system_info = system_info

    def validate(self):
        if self.start_parameters:
            for k in self.start_parameters:
                if k:
                    k.validate()
        if self.system_info:
            for k in self.system_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.custom_session_id is not None:
            result['CustomSessionId'] = self.custom_session_id
        if self.custom_user_id is not None:
            result['CustomUserId'] = self.custom_user_id
        result['StartParameters'] = []
        if self.start_parameters is not None:
            for k in self.start_parameters:
                result['StartParameters'].append(k.to_map() if k else None)
        result['SystemInfo'] = []
        if self.system_info is not None:
            for k in self.system_info:
                result['SystemInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('CustomSessionId') is not None:
            self.custom_session_id = m.get('CustomSessionId')
        if m.get('CustomUserId') is not None:
            self.custom_user_id = m.get('CustomUserId')
        self.start_parameters = []
        if m.get('StartParameters') is not None:
            for k in m.get('StartParameters'):
                temp_model = CreateAppSessionRequestStartParameters()
                self.start_parameters.append(temp_model.from_map(k))
        self.system_info = []
        if m.get('SystemInfo') is not None:
            for k in m.get('SystemInfo'):
                temp_model = CreateAppSessionRequestSystemInfo()
                self.system_info.append(temp_model.from_map(k))
        return self


class CreateAppSessionResponseBody(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_version: str = None,
        custom_session_id: str = None,
        platform_session_id: str = None,
        request_id: str = None,
    ):
        # 应用id
        self.app_id = app_id
        # 应用版本
        self.app_version = app_version
        # 自定义会话id
        self.custom_session_id = custom_session_id
        # 平台会话id
        self.platform_session_id = platform_session_id
        # 请求id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.custom_session_id is not None:
            result['CustomSessionId'] = self.custom_session_id
        if self.platform_session_id is not None:
            result['PlatformSessionId'] = self.platform_session_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('CustomSessionId') is not None:
            self.custom_session_id = m.get('CustomSessionId')
        if m.get('PlatformSessionId') is not None:
            self.platform_session_id = m.get('PlatformSessionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAppSessionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAppSessionResponseBody = None,
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
            temp_model = CreateAppSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppSessionBatchRequestAppInfosStartParameters(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateAppSessionBatchRequestAppInfosSystemInfo(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateAppSessionBatchRequestAppInfos(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_version: str = None,
        client_ip: str = None,
        custom_user_id: str = None,
        customer_session_id: str = None,
        start_parameters: List[CreateAppSessionBatchRequestAppInfosStartParameters] = None,
        system_info: List[CreateAppSessionBatchRequestAppInfosSystemInfo] = None,
    ):
        self.app_id = app_id
        self.app_version = app_version
        self.client_ip = client_ip
        self.custom_user_id = custom_user_id
        self.customer_session_id = customer_session_id
        self.start_parameters = start_parameters
        self.system_info = system_info

    def validate(self):
        if self.start_parameters:
            for k in self.start_parameters:
                if k:
                    k.validate()
        if self.system_info:
            for k in self.system_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.custom_user_id is not None:
            result['CustomUserId'] = self.custom_user_id
        if self.customer_session_id is not None:
            result['CustomerSessionId'] = self.customer_session_id
        result['StartParameters'] = []
        if self.start_parameters is not None:
            for k in self.start_parameters:
                result['StartParameters'].append(k.to_map() if k else None)
        result['SystemInfo'] = []
        if self.system_info is not None:
            for k in self.system_info:
                result['SystemInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('CustomUserId') is not None:
            self.custom_user_id = m.get('CustomUserId')
        if m.get('CustomerSessionId') is not None:
            self.customer_session_id = m.get('CustomerSessionId')
        self.start_parameters = []
        if m.get('StartParameters') is not None:
            for k in m.get('StartParameters'):
                temp_model = CreateAppSessionBatchRequestAppInfosStartParameters()
                self.start_parameters.append(temp_model.from_map(k))
        self.system_info = []
        if m.get('SystemInfo') is not None:
            for k in m.get('SystemInfo'):
                temp_model = CreateAppSessionBatchRequestAppInfosSystemInfo()
                self.system_info.append(temp_model.from_map(k))
        return self


class CreateAppSessionBatchRequest(TeaModel):
    def __init__(
        self,
        app_infos: List[CreateAppSessionBatchRequestAppInfos] = None,
        custom_task_id: str = None,
        timeout: int = None,
    ):
        self.app_infos = app_infos
        self.custom_task_id = custom_task_id
        self.timeout = timeout

    def validate(self):
        if self.app_infos:
            for k in self.app_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppInfos'] = []
        if self.app_infos is not None:
            for k in self.app_infos:
                result['AppInfos'].append(k.to_map() if k else None)
        if self.custom_task_id is not None:
            result['CustomTaskId'] = self.custom_task_id
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_infos = []
        if m.get('AppInfos') is not None:
            for k in m.get('AppInfos'):
                temp_model = CreateAppSessionBatchRequestAppInfos()
                self.app_infos.append(temp_model.from_map(k))
        if m.get('CustomTaskId') is not None:
            self.custom_task_id = m.get('CustomTaskId')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class CreateAppSessionBatchShrinkRequest(TeaModel):
    def __init__(
        self,
        app_infos_shrink: str = None,
        custom_task_id: str = None,
        timeout: int = None,
    ):
        self.app_infos_shrink = app_infos_shrink
        self.custom_task_id = custom_task_id
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_infos_shrink is not None:
            result['AppInfos'] = self.app_infos_shrink
        if self.custom_task_id is not None:
            result['CustomTaskId'] = self.custom_task_id
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInfos') is not None:
            self.app_infos_shrink = m.get('AppInfos')
        if m.get('CustomTaskId') is not None:
            self.custom_task_id = m.get('CustomTaskId')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class CreateAppSessionBatchResponseBody(TeaModel):
    def __init__(
        self,
        custom_task_id: str = None,
        platform_task_id: str = None,
        request_id: str = None,
    ):
        # 自定义会话id
        self.custom_task_id = custom_task_id
        # 平台会话id
        self.platform_task_id = platform_task_id
        # 请求id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_task_id is not None:
            result['CustomTaskId'] = self.custom_task_id
        if self.platform_task_id is not None:
            result['PlatformTaskId'] = self.platform_task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomTaskId') is not None:
            self.custom_task_id = m.get('CustomTaskId')
        if m.get('PlatformTaskId') is not None:
            self.platform_task_id = m.get('PlatformTaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAppSessionBatchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAppSessionBatchResponseBody = None,
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
            temp_model = CreateAppSessionBatchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUploadTaskRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_type: str = None,
        bucket_name: str = None,
        env: str = None,
        file_address: str = None,
        file_size: int = None,
        file_type: str = None,
        progress: float = None,
        region: str = None,
        status: str = None,
        upload_tool_version: str = None,
        upload_type: str = None,
        version_id: str = None,
    ):
        # 应用ID
        self.app_id = app_id
        # 应用类型
        self.app_type = app_type
        # 上传的bucket名称
        self.bucket_name = bucket_name
        # 环境
        self.env = env
        # 游戏链接
        self.file_address = file_address
        # 文件大小
        self.file_size = file_size
        # 上传文件类型
        self.file_type = file_type
        # 上传进度
        self.progress = progress
        # 上传的bucket所在region
        self.region = region
        # 上传状态
        self.status = status
        # 上传工具版本
        self.upload_tool_version = upload_tool_version
        # 上传任务类型
        self.upload_type = upload_type
        # 版本ID
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.env is not None:
            result['Env'] = self.env
        if self.file_address is not None:
            result['FileAddress'] = self.file_address
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.region is not None:
            result['Region'] = self.region
        if self.status is not None:
            result['Status'] = self.status
        if self.upload_tool_version is not None:
            result['UploadToolVersion'] = self.upload_tool_version
        if self.upload_type is not None:
            result['UploadType'] = self.upload_type
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('FileAddress') is not None:
            self.file_address = m.get('FileAddress')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UploadToolVersion') is not None:
            self.upload_tool_version = m.get('UploadToolVersion')
        if m.get('UploadType') is not None:
            self.upload_type = m.get('UploadType')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class CreateUploadTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateUploadTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateUploadTaskResponseBody = None,
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
            temp_model = CreateUploadTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppListResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
    ):
        # 应用ID
        self.app_id = app_id
        # 应用名称
        self.app_name = app_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class GetAppListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetAppListResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetAppListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAppListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAppListResponseBody = None,
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
            temp_model = GetAppListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppSessionRequest(TeaModel):
    def __init__(
        self,
        custom_session_id: str = None,
        platform_session_id: str = None,
    ):
        # 自定义会话id
        self.custom_session_id = custom_session_id
        # 平台会话id
        self.platform_session_id = platform_session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_session_id is not None:
            result['CustomSessionId'] = self.custom_session_id
        if self.platform_session_id is not None:
            result['PlatformSessionId'] = self.platform_session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomSessionId') is not None:
            self.custom_session_id = m.get('CustomSessionId')
        if m.get('PlatformSessionId') is not None:
            self.platform_session_id = m.get('PlatformSessionId')
        return self


class GetAppSessionResponseBodyScheduleInfo(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # key数值，枚举有多个数值，例如： RegionId 大区id ServerIp 服务端 IP ServerPort 端口
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetAppSessionResponseBody(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_version: str = None,
        custom_session_id: str = None,
        platform_session_id: str = None,
        request_id: str = None,
        schedule_info: List[GetAppSessionResponseBodyScheduleInfo] = None,
        status: str = None,
    ):
        # 应用id
        self.app_id = app_id
        # 应用版本
        self.app_version = app_version
        # 自定义会话id
        self.custom_session_id = custom_session_id
        # 平台会话id
        self.platform_session_id = platform_session_id
        # 请求id
        self.request_id = request_id
        self.schedule_info = schedule_info
        # 状态
        self.status = status

    def validate(self):
        if self.schedule_info:
            for k in self.schedule_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.custom_session_id is not None:
            result['CustomSessionId'] = self.custom_session_id
        if self.platform_session_id is not None:
            result['PlatformSessionId'] = self.platform_session_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ScheduleInfo'] = []
        if self.schedule_info is not None:
            for k in self.schedule_info:
                result['ScheduleInfo'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('CustomSessionId') is not None:
            self.custom_session_id = m.get('CustomSessionId')
        if m.get('PlatformSessionId') is not None:
            self.platform_session_id = m.get('PlatformSessionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.schedule_info = []
        if m.get('ScheduleInfo') is not None:
            for k in m.get('ScheduleInfo'):
                temp_model = GetAppSessionResponseBodyScheduleInfo()
                self.schedule_info.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetAppSessionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAppSessionResponseBody = None,
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
            temp_model = GetAppSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNeedUploadFileListRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        env: str = None,
        hash_list: List[str] = None,
        version_id: str = None,
    ):
        # 应用ID
        self.app_id = app_id
        # 环境
        self.env = env
        self.hash_list = hash_list
        # 版本ID
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.env is not None:
            result['Env'] = self.env
        if self.hash_list is not None:
            result['HashList'] = self.hash_list
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('HashList') is not None:
            self.hash_list = m.get('HashList')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class GetNeedUploadFileListResponseBodyData(TeaModel):
    def __init__(
        self,
        err: str = None,
        need_upload_file_list: List[str] = None,
        success: bool = None,
    ):
        # 错误信息
        self.err = err
        # 待上传文件列表
        self.need_upload_file_list = need_upload_file_list
        # 请求结果
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err is not None:
            result['Err'] = self.err
        if self.need_upload_file_list is not None:
            result['NeedUploadFileList'] = self.need_upload_file_list
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Err') is not None:
            self.err = m.get('Err')
        if m.get('NeedUploadFileList') is not None:
            self.need_upload_file_list = m.get('NeedUploadFileList')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetNeedUploadFileListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetNeedUploadFileListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetNeedUploadFileListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetNeedUploadFileListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetNeedUploadFileListResponseBody = None,
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
            temp_model = GetNeedUploadFileListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOssInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        first: str = None,
        second: str = None,
    ):
        self.first = first
        self.second = second

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.first is not None:
            result['First'] = self.first
        if self.second is not None:
            result['Second'] = self.second
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('First') is not None:
            self.first = m.get('First')
        if m.get('Second') is not None:
            self.second = m.get('Second')
        return self


class GetOssInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetOssInfoResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetOssInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetOssInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetOssInfoResponseBody = None,
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
            temp_model = GetOssInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTenantIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTenantIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTenantIdResponseBody = None,
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
            temp_model = GetTenantIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTokenRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        bucket: str = None,
        env: str = None,
        region: str = None,
        version_id: str = None,
    ):
        # 应用ID
        self.app_id = app_id
        # 存储桶
        self.bucket = bucket
        # 环境
        self.env = env
        # 区域ID
        self.region = region
        # 版本ID
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.env is not None:
            result['Env'] = self.env
        if self.region is not None:
            result['Region'] = self.region
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class GetTokenResponseBodyData(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        endpoint: str = None,
        expiration: str = None,
        internal_endpoint: str = None,
        security_token: str = None,
    ):
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.endpoint = endpoint
        self.expiration = expiration
        self.internal_endpoint = internal_endpoint
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        if self.internal_endpoint is not None:
            result['InternalEndpoint'] = self.internal_endpoint
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        if m.get('InternalEndpoint') is not None:
            self.internal_endpoint = m.get('InternalEndpoint')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class GetTokenResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetTokenResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetTokenResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTokenResponseBody = None,
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
            temp_model = GetTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUploadToolUrlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Dict[str, str] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetUploadToolUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetUploadToolUrlResponseBody = None,
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
            temp_model = GetUploadToolUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HasActivateResponseBodyData(TeaModel):
    def __init__(
        self,
        success: bool = None,
    ):
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class HasActivateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: HasActivateResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 业务处理结果Code
        self.code = code
        # 业务对象
        self.data = data
        # 业务处理消息摘要
        self.message = message
        # 操作请求ID
        self.request_id = request_id
        # 业务处理是否成功
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
            temp_model = HasActivateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class HasActivateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: HasActivateResponseBody = None,
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
            temp_model = HasActivateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppSessionsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        custom_session_ids: List[str] = None,
        page_number: int = None,
        page_size: int = None,
        platform_session_ids: List[str] = None,
    ):
        self.app_id = app_id
        # 自定义会话id
        self.custom_session_ids = custom_session_ids
        # 页码
        self.page_number = page_number
        # 分页大小
        self.page_size = page_size
        # 自定义用户id
        self.platform_session_ids = platform_session_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.custom_session_ids is not None:
            result['CustomSessionIds'] = self.custom_session_ids
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.platform_session_ids is not None:
            result['PlatformSessionIds'] = self.platform_session_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CustomSessionIds') is not None:
            self.custom_session_ids = m.get('CustomSessionIds')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PlatformSessionIds') is not None:
            self.platform_session_ids = m.get('PlatformSessionIds')
        return self


class ListAppSessionsResponseBodyAppSessions(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_version: str = None,
        custom_session_id: str = None,
        platform_session_id: str = None,
        status: str = None,
    ):
        # 应用id
        self.app_id = app_id
        # 应用版本
        self.app_version = app_version
        # 自定义会话id
        self.custom_session_id = custom_session_id
        # 平台会话id
        self.platform_session_id = platform_session_id
        # 状态
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.custom_session_id is not None:
            result['CustomSessionId'] = self.custom_session_id
        if self.platform_session_id is not None:
            result['PlatformSessionId'] = self.platform_session_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('CustomSessionId') is not None:
            self.custom_session_id = m.get('CustomSessionId')
        if m.get('PlatformSessionId') is not None:
            self.platform_session_id = m.get('PlatformSessionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListAppSessionsResponseBody(TeaModel):
    def __init__(
        self,
        app_sessions: List[ListAppSessionsResponseBodyAppSessions] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
    ):
        self.app_sessions = app_sessions
        self.page_number = page_number
        self.page_size = page_size
        # 请求id
        self.request_id = request_id

    def validate(self):
        if self.app_sessions:
            for k in self.app_sessions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppSessions'] = []
        if self.app_sessions is not None:
            for k in self.app_sessions:
                result['AppSessions'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_sessions = []
        if m.get('AppSessions') is not None:
            for k in m.get('AppSessions'):
                temp_model = ListAppSessionsResponseBodyAppSessions()
                self.app_sessions.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAppSessionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAppSessionsResponseBody = None,
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
            temp_model = ListAppSessionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PageQueryResourcePackageListRequest(TeaModel):
    def __init__(
        self,
        operator_id: str = None,
        operator_type: str = None,
        package_type: str = None,
        page_number: int = None,
        page_size: int = None,
        query_valid_type: str = None,
    ):
        # 请求操作人Id
        self.operator_id = operator_id
        # 请求操作人类型
        self.operator_type = operator_type
        # 资源包类型,PackageType[CU(cu),code,cssResourceType,desc]
        self.package_type = package_type
        # 当前页码，默认1
        self.page_number = page_number
        # 每页项数，默认20,最大100
        self.page_size = page_size
        # 查询过期的资源包类型,ResourcePackageValidQueryConditionType[All(查询所有资源包),CurrentlyValid(查询当前有效的资源包(已开始，未结束)),PendingValid(未开始,即将生效的资源包),AllValid(已开始未结束 + 即将开始 的资源包),PendingInvalid5m(5min内即将到期的资源包),HasInvalid(已经过期的资源包),queryType,desc]
        self.query_valid_type = query_valid_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_valid_type is not None:
            result['QueryValidType'] = self.query_valid_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryValidType') is not None:
            self.query_valid_type = m.get('QueryValidType')
        return self


class PageQueryResourcePackageListResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        current_amount: int = None,
        gmt_valid_begin: str = None,
        gmt_valid_end: str = None,
        init_amount: int = None,
        package_instance_id: str = None,
        package_type: str = None,
    ):
        # 当前资源包剩余总量
        self.current_amount = current_amount
        # 资源包有效开始时间
        self.gmt_valid_begin = gmt_valid_begin
        # 资源包有效结束时间
        self.gmt_valid_end = gmt_valid_end
        # 当前资源包购买总量
        self.init_amount = init_amount
        # 资源包实例ID
        self.package_instance_id = package_instance_id
        # 资源包类型
        self.package_type = package_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_amount is not None:
            result['CurrentAmount'] = self.current_amount
        if self.gmt_valid_begin is not None:
            result['GmtValidBegin'] = self.gmt_valid_begin
        if self.gmt_valid_end is not None:
            result['GmtValidEnd'] = self.gmt_valid_end
        if self.init_amount is not None:
            result['InitAmount'] = self.init_amount
        if self.package_instance_id is not None:
            result['PackageInstanceId'] = self.package_instance_id
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentAmount') is not None:
            self.current_amount = m.get('CurrentAmount')
        if m.get('GmtValidBegin') is not None:
            self.gmt_valid_begin = m.get('GmtValidBegin')
        if m.get('GmtValidEnd') is not None:
            self.gmt_valid_end = m.get('GmtValidEnd')
        if m.get('InitAmount') is not None:
            self.init_amount = m.get('InitAmount')
        if m.get('PackageInstanceId') is not None:
            self.package_instance_id = m.get('PackageInstanceId')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        return self


class PageQueryResourcePackageListResponseBodyData(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        pages: int = None,
        records: List[PageQueryResourcePackageListResponseBodyDataRecords] = None,
        total_count: int = None,
    ):
        # 当前页码，默认1
        self.page_number = page_number
        # 每页项数，默认20,最大100
        self.page_size = page_size
        # 总页数
        self.pages = pages
        # 结果集
        self.records = records
        # 总共项数
        self.total_count = total_count

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pages is not None:
            result['Pages'] = self.pages
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = PageQueryResourcePackageListResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class PageQueryResourcePackageListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: PageQueryResourcePackageListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 业务处理结果Code
        self.code = code
        # 业务对象
        self.data = data
        # 业务处理消息摘要
        self.message = message
        # 操作请求ID
        self.request_id = request_id
        # 业务处理是否成功
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
            temp_model = PageQueryResourcePackageListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PageQueryResourcePackageListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PageQueryResourcePackageListResponseBody = None,
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
            temp_model = PageQueryResourcePackageListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAdaptRecordsRequest(TeaModel):
    def __init__(
        self,
        app_version_id: str = None,
        request_app: str = None,
    ):
        self.app_version_id = app_version_id
        self.request_app = request_app

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        if self.request_app is not None:
            result['RequestApp'] = self.request_app
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        if m.get('RequestApp') is not None:
            self.request_app = m.get('RequestApp')
        return self


class QueryAdaptRecordsResponseBodyDataAdaptRecordsAdaptTarget(TeaModel):
    def __init__(
        self,
        bit_rate: int = None,
        frame_rate: int = None,
        resolution: str = None,
        start_program: str = None,
    ):
        self.bit_rate = bit_rate
        self.frame_rate = frame_rate
        self.resolution = resolution
        self.start_program = start_program

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bit_rate is not None:
            result['BitRate'] = self.bit_rate
        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        if self.start_program is not None:
            result['StartProgram'] = self.start_program
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BitRate') is not None:
            self.bit_rate = m.get('BitRate')
        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        if m.get('StartProgram') is not None:
            self.start_program = m.get('StartProgram')
        return self


class QueryAdaptRecordsResponseBodyDataAdaptRecordsCalculationEvaluationInfoCpu(TeaModel):
    def __init__(
        self,
        average: float = None,
        maximum: float = None,
        minimum: float = None,
        number_of_cores: float = None,
        quantile_80: float = None,
    ):
        self.average = average
        self.maximum = maximum
        self.minimum = minimum
        self.number_of_cores = number_of_cores
        self.quantile_80 = quantile_80

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.average is not None:
            result['Average'] = self.average
        if self.maximum is not None:
            result['Maximum'] = self.maximum
        if self.minimum is not None:
            result['Minimum'] = self.minimum
        if self.number_of_cores is not None:
            result['NumberOfCores'] = self.number_of_cores
        if self.quantile_80 is not None:
            result['Quantile80'] = self.quantile_80
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Average') is not None:
            self.average = m.get('Average')
        if m.get('Maximum') is not None:
            self.maximum = m.get('Maximum')
        if m.get('Minimum') is not None:
            self.minimum = m.get('Minimum')
        if m.get('NumberOfCores') is not None:
            self.number_of_cores = m.get('NumberOfCores')
        if m.get('Quantile80') is not None:
            self.quantile_80 = m.get('Quantile80')
        return self


class QueryAdaptRecordsResponseBodyDataAdaptRecordsCalculationEvaluationInfoGpuGpuUsedutilization(TeaModel):
    def __init__(
        self,
        average: float = None,
        maximum: float = None,
        minimum: float = None,
        number_of_cores: float = None,
        quantile_80: float = None,
    ):
        self.average = average
        self.maximum = maximum
        self.minimum = minimum
        self.number_of_cores = number_of_cores
        self.quantile_80 = quantile_80

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.average is not None:
            result['Average'] = self.average
        if self.maximum is not None:
            result['Maximum'] = self.maximum
        if self.minimum is not None:
            result['Minimum'] = self.minimum
        if self.number_of_cores is not None:
            result['NumberOfCores'] = self.number_of_cores
        if self.quantile_80 is not None:
            result['Quantile80'] = self.quantile_80
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Average') is not None:
            self.average = m.get('Average')
        if m.get('Maximum') is not None:
            self.maximum = m.get('Maximum')
        if m.get('Minimum') is not None:
            self.minimum = m.get('Minimum')
        if m.get('NumberOfCores') is not None:
            self.number_of_cores = m.get('NumberOfCores')
        if m.get('Quantile80') is not None:
            self.quantile_80 = m.get('Quantile80')
        return self


class QueryAdaptRecordsResponseBodyDataAdaptRecordsCalculationEvaluationInfoGpuMemUsedutilization(TeaModel):
    def __init__(
        self,
        average: float = None,
        maximum: float = None,
        minimum: float = None,
        quantile_80: float = None,
        total: float = None,
    ):
        self.average = average
        self.maximum = maximum
        self.minimum = minimum
        self.quantile_80 = quantile_80
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.average is not None:
            result['Average'] = self.average
        if self.maximum is not None:
            result['Maximum'] = self.maximum
        if self.minimum is not None:
            result['Minimum'] = self.minimum
        if self.quantile_80 is not None:
            result['Quantile80'] = self.quantile_80
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Average') is not None:
            self.average = m.get('Average')
        if m.get('Maximum') is not None:
            self.maximum = m.get('Maximum')
        if m.get('Minimum') is not None:
            self.minimum = m.get('Minimum')
        if m.get('Quantile80') is not None:
            self.quantile_80 = m.get('Quantile80')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryAdaptRecordsResponseBodyDataAdaptRecordsCalculationEvaluationInfoGpu(TeaModel):
    def __init__(
        self,
        gpu_usedutilization: QueryAdaptRecordsResponseBodyDataAdaptRecordsCalculationEvaluationInfoGpuGpuUsedutilization = None,
        mem_usedutilization: QueryAdaptRecordsResponseBodyDataAdaptRecordsCalculationEvaluationInfoGpuMemUsedutilization = None,
    ):
        self.gpu_usedutilization = gpu_usedutilization
        self.mem_usedutilization = mem_usedutilization

    def validate(self):
        if self.gpu_usedutilization:
            self.gpu_usedutilization.validate()
        if self.mem_usedutilization:
            self.mem_usedutilization.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gpu_usedutilization is not None:
            result['GpuUsedutilization'] = self.gpu_usedutilization.to_map()
        if self.mem_usedutilization is not None:
            result['MemUsedutilization'] = self.mem_usedutilization.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GpuUsedutilization') is not None:
            temp_model = QueryAdaptRecordsResponseBodyDataAdaptRecordsCalculationEvaluationInfoGpuGpuUsedutilization()
            self.gpu_usedutilization = temp_model.from_map(m['GpuUsedutilization'])
        if m.get('MemUsedutilization') is not None:
            temp_model = QueryAdaptRecordsResponseBodyDataAdaptRecordsCalculationEvaluationInfoGpuMemUsedutilization()
            self.mem_usedutilization = temp_model.from_map(m['MemUsedutilization'])
        return self


class QueryAdaptRecordsResponseBodyDataAdaptRecordsCalculationEvaluationInfoMem(TeaModel):
    def __init__(
        self,
        average: float = None,
        maximum: float = None,
        minimum: float = None,
        quantile_80: float = None,
        total: float = None,
    ):
        self.average = average
        self.maximum = maximum
        self.minimum = minimum
        self.quantile_80 = quantile_80
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.average is not None:
            result['Average'] = self.average
        if self.maximum is not None:
            result['Maximum'] = self.maximum
        if self.minimum is not None:
            result['Minimum'] = self.minimum
        if self.quantile_80 is not None:
            result['Quantile80'] = self.quantile_80
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Average') is not None:
            self.average = m.get('Average')
        if m.get('Maximum') is not None:
            self.maximum = m.get('Maximum')
        if m.get('Minimum') is not None:
            self.minimum = m.get('Minimum')
        if m.get('Quantile80') is not None:
            self.quantile_80 = m.get('Quantile80')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryAdaptRecordsResponseBodyDataAdaptRecordsCalculationEvaluationInfo(TeaModel):
    def __init__(
        self,
        cpu: QueryAdaptRecordsResponseBodyDataAdaptRecordsCalculationEvaluationInfoCpu = None,
        gpu: QueryAdaptRecordsResponseBodyDataAdaptRecordsCalculationEvaluationInfoGpu = None,
        mem: QueryAdaptRecordsResponseBodyDataAdaptRecordsCalculationEvaluationInfoMem = None,
    ):
        self.cpu = cpu
        self.gpu = gpu
        self.mem = mem

    def validate(self):
        if self.cpu:
            self.cpu.validate()
        if self.gpu:
            self.gpu.validate()
        if self.mem:
            self.mem.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu.to_map()
        if self.gpu is not None:
            result['Gpu'] = self.gpu.to_map()
        if self.mem is not None:
            result['Mem'] = self.mem.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            temp_model = QueryAdaptRecordsResponseBodyDataAdaptRecordsCalculationEvaluationInfoCpu()
            self.cpu = temp_model.from_map(m['Cpu'])
        if m.get('Gpu') is not None:
            temp_model = QueryAdaptRecordsResponseBodyDataAdaptRecordsCalculationEvaluationInfoGpu()
            self.gpu = temp_model.from_map(m['Gpu'])
        if m.get('Mem') is not None:
            temp_model = QueryAdaptRecordsResponseBodyDataAdaptRecordsCalculationEvaluationInfoMem()
            self.mem = temp_model.from_map(m['Mem'])
        return self


class QueryAdaptRecordsResponseBodyDataAdaptRecordsServerInfo(TeaModel):
    def __init__(
        self,
        cpu_type: str = None,
        gpu_type: str = None,
        name: str = None,
    ):
        self.cpu_type = cpu_type
        self.gpu_type = gpu_type
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_type is not None:
            result['CpuType'] = self.cpu_type
        if self.gpu_type is not None:
            result['GpuType'] = self.gpu_type
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuType') is not None:
            self.cpu_type = m.get('CpuType')
        if m.get('GpuType') is not None:
            self.gpu_type = m.get('GpuType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class QueryAdaptRecordsResponseBodyDataAdaptRecords(TeaModel):
    def __init__(
        self,
        adapt_apply_id: int = None,
        adapt_record_id: int = None,
        adapt_status: str = None,
        adapt_target: QueryAdaptRecordsResponseBodyDataAdaptRecordsAdaptTarget = None,
        app_id: str = None,
        app_version_id: str = None,
        calculation_evaluation_info: QueryAdaptRecordsResponseBodyDataAdaptRecordsCalculationEvaluationInfo = None,
        consume_cu: float = None,
        container_type: str = None,
        file_download_path: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        image_type: str = None,
        is_must_select: bool = None,
        isv: str = None,
        max_concurrency: int = None,
        memo: str = None,
        priority: int = None,
        server_info: QueryAdaptRecordsResponseBodyDataAdaptRecordsServerInfo = None,
        tenant_id: int = None,
        vm_type: str = None,
    ):
        self.adapt_apply_id = adapt_apply_id
        self.adapt_record_id = adapt_record_id
        self.adapt_status = adapt_status
        self.adapt_target = adapt_target
        self.app_id = app_id
        self.app_version_id = app_version_id
        self.calculation_evaluation_info = calculation_evaluation_info
        self.consume_cu = consume_cu
        # 蔚领：1 独占虚机，2 支持多开 (EXCLUSIVE: 独占虚机, SHARED: 支持多开)
        self.container_type = container_type
        self.file_download_path = file_download_path
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.image_type = image_type
        self.is_must_select = is_must_select
        self.isv = isv
        self.max_concurrency = max_concurrency
        self.memo = memo
        self.priority = priority
        self.server_info = server_info
        self.tenant_id = tenant_id
        self.vm_type = vm_type

    def validate(self):
        if self.adapt_target:
            self.adapt_target.validate()
        if self.calculation_evaluation_info:
            self.calculation_evaluation_info.validate()
        if self.server_info:
            self.server_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adapt_apply_id is not None:
            result['AdaptApplyId'] = self.adapt_apply_id
        if self.adapt_record_id is not None:
            result['AdaptRecordId'] = self.adapt_record_id
        if self.adapt_status is not None:
            result['AdaptStatus'] = self.adapt_status
        if self.adapt_target is not None:
            result['AdaptTarget'] = self.adapt_target.to_map()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        if self.calculation_evaluation_info is not None:
            result['CalculationEvaluationInfo'] = self.calculation_evaluation_info.to_map()
        if self.consume_cu is not None:
            result['ConsumeCu'] = self.consume_cu
        if self.container_type is not None:
            result['ContainerType'] = self.container_type
        if self.file_download_path is not None:
            result['FileDownloadPath'] = self.file_download_path
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.is_must_select is not None:
            result['IsMustSelect'] = self.is_must_select
        if self.isv is not None:
            result['Isv'] = self.isv
        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency
        if self.memo is not None:
            result['Memo'] = self.memo
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.server_info is not None:
            result['ServerInfo'] = self.server_info.to_map()
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.vm_type is not None:
            result['VmType'] = self.vm_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdaptApplyId') is not None:
            self.adapt_apply_id = m.get('AdaptApplyId')
        if m.get('AdaptRecordId') is not None:
            self.adapt_record_id = m.get('AdaptRecordId')
        if m.get('AdaptStatus') is not None:
            self.adapt_status = m.get('AdaptStatus')
        if m.get('AdaptTarget') is not None:
            temp_model = QueryAdaptRecordsResponseBodyDataAdaptRecordsAdaptTarget()
            self.adapt_target = temp_model.from_map(m['AdaptTarget'])
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        if m.get('CalculationEvaluationInfo') is not None:
            temp_model = QueryAdaptRecordsResponseBodyDataAdaptRecordsCalculationEvaluationInfo()
            self.calculation_evaluation_info = temp_model.from_map(m['CalculationEvaluationInfo'])
        if m.get('ConsumeCu') is not None:
            self.consume_cu = m.get('ConsumeCu')
        if m.get('ContainerType') is not None:
            self.container_type = m.get('ContainerType')
        if m.get('FileDownloadPath') is not None:
            self.file_download_path = m.get('FileDownloadPath')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('IsMustSelect') is not None:
            self.is_must_select = m.get('IsMustSelect')
        if m.get('Isv') is not None:
            self.isv = m.get('Isv')
        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')
        if m.get('Memo') is not None:
            self.memo = m.get('Memo')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ServerInfo') is not None:
            temp_model = QueryAdaptRecordsResponseBodyDataAdaptRecordsServerInfo()
            self.server_info = temp_model.from_map(m['ServerInfo'])
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('VmType') is not None:
            self.vm_type = m.get('VmType')
        return self


class QueryAdaptRecordsResponseBodyData(TeaModel):
    def __init__(
        self,
        adapt_apply_id: int = None,
        adapt_records: List[QueryAdaptRecordsResponseBodyDataAdaptRecords] = None,
        app_id: str = None,
        app_name: str = None,
        app_type: str = None,
        app_version_id: str = None,
        app_version_name: str = None,
        app_version_serviceype: str = None,
        tenant_id: int = None,
        tenant_name: str = None,
    ):
        self.adapt_apply_id = adapt_apply_id
        self.adapt_records = adapt_records
        self.app_id = app_id
        self.app_name = app_name
        self.app_type = app_type
        self.app_version_id = app_version_id
        self.app_version_name = app_version_name
        self.app_version_serviceype = app_version_serviceype
        self.tenant_id = tenant_id
        self.tenant_name = tenant_name

    def validate(self):
        if self.adapt_records:
            for k in self.adapt_records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adapt_apply_id is not None:
            result['AdaptApplyId'] = self.adapt_apply_id
        result['AdaptRecords'] = []
        if self.adapt_records is not None:
            for k in self.adapt_records:
                result['AdaptRecords'].append(k.to_map() if k else None)
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        if self.app_version_name is not None:
            result['AppVersionName'] = self.app_version_name
        if self.app_version_serviceype is not None:
            result['AppVersionServiceype'] = self.app_version_serviceype
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdaptApplyId') is not None:
            self.adapt_apply_id = m.get('AdaptApplyId')
        self.adapt_records = []
        if m.get('AdaptRecords') is not None:
            for k in m.get('AdaptRecords'):
                temp_model = QueryAdaptRecordsResponseBodyDataAdaptRecords()
                self.adapt_records.append(temp_model.from_map(k))
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        if m.get('AppVersionName') is not None:
            self.app_version_name = m.get('AppVersionName')
        if m.get('AppVersionServiceype') is not None:
            self.app_version_serviceype = m.get('AppVersionServiceype')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        return self


class QueryAdaptRecordsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryAdaptRecordsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryAdaptRecordsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryAdaptRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryAdaptRecordsResponseBody = None,
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
            temp_model = QueryAdaptRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUploadProgressRequest(TeaModel):
    def __init__(
        self,
        query_upload_progress_requests: str = None,
    ):
        self.query_upload_progress_requests = query_upload_progress_requests

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query_upload_progress_requests is not None:
            result['QueryUploadProgressRequests'] = self.query_upload_progress_requests
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QueryUploadProgressRequests') is not None:
            self.query_upload_progress_requests = m.get('QueryUploadProgressRequests')
        return self


class QueryUploadProgressResponseBodyDataContentVersions(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        progress: float = None,
        tenant_id: int = None,
        version_id: str = None,
    ):
        self.app_id = app_id
        self.progress = progress
        self.tenant_id = tenant_id
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class QueryUploadProgressResponseBodyDataContent(TeaModel):
    def __init__(
        self,
        versions: List[QueryUploadProgressResponseBodyDataContentVersions] = None,
    ):
        self.versions = versions

    def validate(self):
        if self.versions:
            for k in self.versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Versions'] = []
        if self.versions is not None:
            for k in self.versions:
                result['Versions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.versions = []
        if m.get('Versions') is not None:
            for k in m.get('Versions'):
                temp_model = QueryUploadProgressResponseBodyDataContentVersions()
                self.versions.append(temp_model.from_map(k))
        return self


class QueryUploadProgressResponseBodyData(TeaModel):
    def __init__(
        self,
        code: str = None,
        content: QueryUploadProgressResponseBodyDataContent = None,
        message: str = None,
    ):
        # 查询结果
        self.code = code
        # 进度信息
        self.content = content
        # 查询信息
        self.message = message

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content.to_map()
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Content') is not None:
            temp_model = QueryUploadProgressResponseBodyDataContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class QueryUploadProgressResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryUploadProgressResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryUploadProgressResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryUploadProgressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryUploadProgressResponseBody = None,
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
            temp_model = QueryUploadProgressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecordFinishedFileRequestFileFingerprintDTOList(TeaModel):
    def __init__(
        self,
        file_hash: str = None,
        file_size: int = None,
    ):
        # 文件hash
        self.file_hash = file_hash
        # 文件大小
        self.file_size = file_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_hash is not None:
            result['FileHash'] = self.file_hash
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileHash') is not None:
            self.file_hash = m.get('FileHash')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        return self


class RecordFinishedFileRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        bucket_name: str = None,
        env: str = None,
        file_fingerprint_dtolist: List[RecordFinishedFileRequestFileFingerprintDTOList] = None,
        file_size: int = None,
        file_type: str = None,
        region: str = None,
        tool_version: str = None,
        version_id: str = None,
    ):
        # 应用ID
        self.app_id = app_id
        # 上传的bucket名称
        self.bucket_name = bucket_name
        # 环境
        self.env = env
        # 用于pop传入的文件指纹信息
        self.file_fingerprint_dtolist = file_fingerprint_dtolist
        # 文件大小
        self.file_size = file_size
        # 上传文件类型
        self.file_type = file_type
        # 上传的bucket所在region
        self.region = region
        # 上传工具版本
        self.tool_version = tool_version
        # 版本ID
        self.version_id = version_id

    def validate(self):
        if self.file_fingerprint_dtolist:
            for k in self.file_fingerprint_dtolist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.env is not None:
            result['Env'] = self.env
        result['FileFingerprintDTOList'] = []
        if self.file_fingerprint_dtolist is not None:
            for k in self.file_fingerprint_dtolist:
                result['FileFingerprintDTOList'].append(k.to_map() if k else None)
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.region is not None:
            result['Region'] = self.region
        if self.tool_version is not None:
            result['ToolVersion'] = self.tool_version
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        self.file_fingerprint_dtolist = []
        if m.get('FileFingerprintDTOList') is not None:
            for k in m.get('FileFingerprintDTOList'):
                temp_model = RecordFinishedFileRequestFileFingerprintDTOList()
                self.file_fingerprint_dtolist.append(temp_model.from_map(k))
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ToolVersion') is not None:
            self.tool_version = m.get('ToolVersion')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class RecordFinishedFileResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecordFinishedFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecordFinishedFileResponseBody = None,
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
            temp_model = RecordFinishedFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReplicateVersionRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        source_version_id: str = None,
        target_version_id: str = None,
        tenant_id: int = None,
    ):
        # 应用Id
        self.app_id = app_id
        # 源头版本Id
        self.source_version_id = source_version_id
        # 复制目标版本Id
        self.target_version_id = target_version_id
        # 租户Id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.source_version_id is not None:
            result['SourceVersionId'] = self.source_version_id
        if self.target_version_id is not None:
            result['TargetVersionId'] = self.target_version_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('SourceVersionId') is not None:
            self.source_version_id = m.get('SourceVersionId')
        if m.get('TargetVersionId') is not None:
            self.target_version_id = m.get('TargetVersionId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ReplicateVersionResponseBodyData(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # 复制结果
        self.code = code
        # 复制结果信息
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class ReplicateVersionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ReplicateVersionResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ReplicateVersionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReplicateVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReplicateVersionResponseBody = None,
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
            temp_model = ReplicateVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReportUploadProgressRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        env: str = None,
        progress: float = None,
        version_id: str = None,
    ):
        # 应用ID
        self.app_id = app_id
        # 环境
        self.env = env
        # 上传进度
        self.progress = progress
        # 版本ID
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.env is not None:
            result['Env'] = self.env
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class ReportUploadProgressResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReportUploadProgressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReportUploadProgressResponseBody = None,
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
            temp_model = ReportUploadProgressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReportUploadResultRequestFileFingerprintDTOList(TeaModel):
    def __init__(
        self,
        file_hash: str = None,
        file_size: int = None,
    ):
        # 文件hash
        self.file_hash = file_hash
        # 文件大小
        self.file_size = file_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_hash is not None:
            result['FileHash'] = self.file_hash
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileHash') is not None:
            self.file_hash = m.get('FileHash')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        return self


class ReportUploadResultRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        bucket_name: str = None,
        env: str = None,
        file_fingerprint_dtolist: List[ReportUploadResultRequestFileFingerprintDTOList] = None,
        file_size: int = None,
        file_type: str = None,
        region: str = None,
        tool_version: str = None,
        version_id: str = None,
    ):
        # 应用ID
        self.app_id = app_id
        # 上传的bucket名称
        self.bucket_name = bucket_name
        # 环境
        self.env = env
        # 用于pop传入的文件指纹信息
        self.file_fingerprint_dtolist = file_fingerprint_dtolist
        # 文件大小
        self.file_size = file_size
        # 上传文件类型
        self.file_type = file_type
        # 上传的bucket所在region
        self.region = region
        # 上传工具版本
        self.tool_version = tool_version
        # 版本ID
        self.version_id = version_id

    def validate(self):
        if self.file_fingerprint_dtolist:
            for k in self.file_fingerprint_dtolist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.env is not None:
            result['Env'] = self.env
        result['FileFingerprintDTOList'] = []
        if self.file_fingerprint_dtolist is not None:
            for k in self.file_fingerprint_dtolist:
                result['FileFingerprintDTOList'].append(k.to_map() if k else None)
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.region is not None:
            result['Region'] = self.region
        if self.tool_version is not None:
            result['ToolVersion'] = self.tool_version
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        self.file_fingerprint_dtolist = []
        if m.get('FileFingerprintDTOList') is not None:
            for k in m.get('FileFingerprintDTOList'):
                temp_model = ReportUploadResultRequestFileFingerprintDTOList()
                self.file_fingerprint_dtolist.append(temp_model.from_map(k))
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ToolVersion') is not None:
            self.tool_version = m.get('ToolVersion')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class ReportUploadResultResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReportUploadResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReportUploadResultResponseBody = None,
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
            temp_model = ReportUploadResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReportUploadStatusRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        env: str = None,
        memo: str = None,
        status: str = None,
        version_id: str = None,
    ):
        # 应用ID
        self.app_id = app_id
        # 环境
        self.env = env
        # 备注信息
        self.memo = memo
        # 上传状态
        self.status = status
        # 版本ID
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.env is not None:
            result['Env'] = self.env
        if self.memo is not None:
            result['Memo'] = self.memo
        if self.status is not None:
            result['Status'] = self.status
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('Memo') is not None:
            self.memo = m.get('Memo')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class ReportUploadStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReportUploadStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReportUploadStatusResponseBody = None,
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
            temp_model = ReportUploadStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopAppSessionRequest(TeaModel):
    def __init__(
        self,
        custom_session_id: str = None,
        platform_session_id: str = None,
    ):
        # 自定义会话id
        self.custom_session_id = custom_session_id
        # 自定义用户id
        self.platform_session_id = platform_session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_session_id is not None:
            result['CustomSessionId'] = self.custom_session_id
        if self.platform_session_id is not None:
            result['PlatformSessionId'] = self.platform_session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomSessionId') is not None:
            self.custom_session_id = m.get('CustomSessionId')
        if m.get('PlatformSessionId') is not None:
            self.platform_session_id = m.get('PlatformSessionId')
        return self


class StopAppSessionResponseBody(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_version: str = None,
        custom_session_id: str = None,
        platform_session_id: str = None,
        request_id: str = None,
    ):
        # 应用id
        self.app_id = app_id
        # 应用版本
        self.app_version = app_version
        # 自定义会话id
        self.custom_session_id = custom_session_id
        # 平台会话id
        self.platform_session_id = platform_session_id
        # 请求id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.custom_session_id is not None:
            result['CustomSessionId'] = self.custom_session_id
        if self.platform_session_id is not None:
            result['PlatformSessionId'] = self.platform_session_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('CustomSessionId') is not None:
            self.custom_session_id = m.get('CustomSessionId')
        if m.get('PlatformSessionId') is not None:
            self.platform_session_id = m.get('PlatformSessionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopAppSessionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopAppSessionResponseBody = None,
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
            temp_model = StopAppSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TotalAppliedConsumStatRequest(TeaModel):
    def __init__(
        self,
        operator_id: str = None,
        operator_type: str = None,
        package_type: str = None,
        query_end_date: str = None,
        query_start_date: str = None,
    ):
        # 请求操作人Id
        self.operator_id = operator_id
        # 请求操作人类型
        self.operator_type = operator_type
        # 资源类型,PackageType[CU(cu),code,cssResourceType,desc]
        self.package_type = package_type
        # 查询结束时间
        self.query_end_date = query_end_date
        # 查询开始时间
        self.query_start_date = query_start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.query_end_date is not None:
            result['QueryEndDate'] = self.query_end_date
        if self.query_start_date is not None:
            result['QueryStartDate'] = self.query_start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('QueryEndDate') is not None:
            self.query_end_date = m.get('QueryEndDate')
        if m.get('QueryStartDate') is not None:
            self.query_start_date = m.get('QueryStartDate')
        return self


class TotalAppliedConsumStatResponseBodyData(TeaModel):
    def __init__(
        self,
        applied_id: str = None,
        consumption_cu: int = None,
        stat_date: str = None,
    ):
        # 应用ID
        self.applied_id = applied_id
        # 分钟级消耗CU
        self.consumption_cu = consumption_cu
        # 统计日期
        self.stat_date = stat_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applied_id is not None:
            result['AppliedId'] = self.applied_id
        if self.consumption_cu is not None:
            result['ConsumptionCu'] = self.consumption_cu
        if self.stat_date is not None:
            result['StatDate'] = self.stat_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppliedId') is not None:
            self.applied_id = m.get('AppliedId')
        if m.get('ConsumptionCu') is not None:
            self.consumption_cu = m.get('ConsumptionCu')
        if m.get('StatDate') is not None:
            self.stat_date = m.get('StatDate')
        return self


class TotalAppliedConsumStatResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[TotalAppliedConsumStatResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 业务处理结果Code
        self.code = code
        # 业务对象
        self.data = data
        # 业务处理消息摘要
        self.message = message
        # 操作请求ID
        self.request_id = request_id
        # 业务处理是否成功
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
                temp_model = TotalAppliedConsumStatResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TotalAppliedConsumStatResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TotalAppliedConsumStatResponseBody = None,
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
            temp_model = TotalAppliedConsumStatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TotalAppliedNearRealStatRequest(TeaModel):
    def __init__(
        self,
        operator_id: str = None,
        operator_type: str = None,
        order_by: str = None,
        package_type: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # 请求操作人Id
        self.operator_id = operator_id
        # 请求操作人类型
        self.operator_type = operator_type
        # 排序类型。默认：AppliedConcurrency_Desc,AppliedNearRealOrderConditionType[AppliedConcurrency_Desc(AppliedConcurrency_Desc,根据实时并发路数降序排列),AppliedConcurrency_Asc(AppliedConcurrency_Asc,根据实时并发路数升序排列),AppliedConsumptionCu_Desc(AppliedConsumptionCu_Desc,根据实时CU消耗降序排列),AppliedConsumptionCu_Asc(AppliedConsumptionCu_Asc,根据实时CU消耗升序排列),orderByType,desc]
        self.order_by = order_by
        # 资源类型,PackageType[CU(cu),code,cssResourceType,desc]
        self.package_type = package_type
        # 当前页码，默认1
        self.page_number = page_number
        # 每页项数，默认20,最大100
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class TotalAppliedNearRealStatResponseBodyData(TeaModel):
    def __init__(
        self,
        total_concurrency: int = None,
        total_consumption_cu: float = None,
    ):
        # 实时消耗并发
        self.total_concurrency = total_concurrency
        # 实时消耗CU
        self.total_consumption_cu = total_consumption_cu

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_concurrency is not None:
            result['TotalConcurrency'] = self.total_concurrency
        if self.total_consumption_cu is not None:
            result['TotalConsumptionCu'] = self.total_consumption_cu
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalConcurrency') is not None:
            self.total_concurrency = m.get('TotalConcurrency')
        if m.get('TotalConsumptionCu') is not None:
            self.total_consumption_cu = m.get('TotalConsumptionCu')
        return self


class TotalAppliedNearRealStatResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: TotalAppliedNearRealStatResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 业务处理结果Code
        self.code = code
        # 业务对象
        self.data = data
        # 业务处理消息摘要
        self.message = message
        # 操作请求ID
        self.request_id = request_id
        # 业务处理是否成功
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
            temp_model = TotalAppliedNearRealStatResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TotalAppliedNearRealStatResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TotalAppliedNearRealStatResponseBody = None,
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
            temp_model = TotalAppliedNearRealStatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TotalQueryResourcePackageRequest(TeaModel):
    def __init__(
        self,
        operator_id: str = None,
        operator_type: str = None,
        package_type: str = None,
    ):
        # 请求操作人Id
        self.operator_id = operator_id
        # 请求操作人类型
        self.operator_type = operator_type
        # 资源包类型,PackageType[CU(cu),code,cssResourceType,desc]
        self.package_type = package_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        return self


class TotalQueryResourcePackageResponseBodyData(TeaModel):
    def __init__(
        self,
        tenant_uid: str = None,
        total_amount: int = None,
        total_date: str = None,
    ):
        # 租户UserId
        self.tenant_uid = tenant_uid
        # 当前所有有效资源包总量
        self.total_amount = total_amount
        # 计算时间
        self.total_date = total_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_uid is not None:
            result['TenantUid'] = self.tenant_uid
        if self.total_amount is not None:
            result['TotalAmount'] = self.total_amount
        if self.total_date is not None:
            result['TotalDate'] = self.total_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TenantUid') is not None:
            self.tenant_uid = m.get('TenantUid')
        if m.get('TotalAmount') is not None:
            self.total_amount = m.get('TotalAmount')
        if m.get('TotalDate') is not None:
            self.total_date = m.get('TotalDate')
        return self


class TotalQueryResourcePackageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: TotalQueryResourcePackageResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 业务处理结果Code
        self.code = code
        # 业务对象
        self.data = data
        # 业务处理消息摘要
        self.message = message
        # 操作请求ID
        self.request_id = request_id
        # 业务处理是否成功
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
            temp_model = TotalQueryResourcePackageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TotalQueryResourcePackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TotalQueryResourcePackageResponseBody = None,
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
            temp_model = TotalQueryResourcePackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


