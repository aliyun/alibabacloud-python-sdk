# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class ListAppTemplateDictsResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        max_results: int = None,
        module: List[main_models.ListAppTemplateDictsResponseBodyModule] = None,
        next_token: str = None,
        request_id: str = None,
        root_error_code: str = None,
        root_error_msg: str = None,
        synchro: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.allow_retry = allow_retry
        self.app_name = app_name
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_args = error_args
        self.max_results = max_results
        self.module = module
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        self.root_error_code = root_error_code
        self.root_error_msg = root_error_msg
        self.synchro = synchro

    def validate(self):
        if self.module:
            for v1 in self.module:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.error_args is not None:
            result['ErrorArgs'] = self.error_args

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        result['Module'] = []
        if self.module is not None:
            for k1 in self.module:
                result['Module'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.root_error_code is not None:
            result['RootErrorCode'] = self.root_error_code

        if self.root_error_msg is not None:
            result['RootErrorMsg'] = self.root_error_msg

        if self.synchro is not None:
            result['Synchro'] = self.synchro

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrorArgs') is not None:
            self.error_args = m.get('ErrorArgs')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        self.module = []
        if m.get('Module') is not None:
            for k1 in m.get('Module'):
                temp_model = main_models.ListAppTemplateDictsResponseBodyModule()
                self.module.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RootErrorCode') is not None:
            self.root_error_code = m.get('RootErrorCode')

        if m.get('RootErrorMsg') is not None:
            self.root_error_msg = m.get('RootErrorMsg')

        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')

        return self

class ListAppTemplateDictsResponseBodyModule(DaraModel):
    def __init__(
        self,
        dict_code: str = None,
        dict_label: str = None,
        dict_type: str = None,
        dict_value: str = None,
        has_templates: bool = None,
        sort_order: int = None,
    ):
        self.dict_code = dict_code
        self.dict_label = dict_label
        self.dict_type = dict_type
        self.dict_value = dict_value
        self.has_templates = has_templates
        self.sort_order = sort_order

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dict_code is not None:
            result['DictCode'] = self.dict_code

        if self.dict_label is not None:
            result['DictLabel'] = self.dict_label

        if self.dict_type is not None:
            result['DictType'] = self.dict_type

        if self.dict_value is not None:
            result['DictValue'] = self.dict_value

        if self.has_templates is not None:
            result['HasTemplates'] = self.has_templates

        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DictCode') is not None:
            self.dict_code = m.get('DictCode')

        if m.get('DictLabel') is not None:
            self.dict_label = m.get('DictLabel')

        if m.get('DictType') is not None:
            self.dict_type = m.get('DictType')

        if m.get('DictValue') is not None:
            self.dict_value = m.get('DictValue')

        if m.get('HasTemplates') is not None:
            self.has_templates = m.get('HasTemplates')

        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')

        return self

