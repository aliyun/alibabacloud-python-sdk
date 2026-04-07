# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class GetExtensionResponseBody(DaraModel):
    def __init__(
        self,
        extension: main_models.GetExtensionResponseBodyExtension = None,
        request_id: str = None,
    ):
        # The details of the extension.
        self.extension = extension
        # The request ID. You can use the request ID to query logs and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.extension:
            self.extension.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extension is not None:
            result['Extension'] = self.extension.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extension') is not None:
            temp_model = main_models.GetExtensionResponseBodyExtension()
            self.extension = temp_model.from_map(m.get('Extension'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetExtensionResponseBodyExtension(DaraModel):
    def __init__(
        self,
        bind_event_list: List[main_models.GetExtensionResponseBodyExtensionBindEventList] = None,
        detail_url: str = None,
        event_category_list: List[main_models.GetExtensionResponseBodyExtensionEventCategoryList] = None,
        extension_code: str = None,
        extension_desc: str = None,
        extension_name: str = None,
        help_doc_url: str = None,
        option_setting: str = None,
        parameter_setting: str = None,
        project_testing: int = None,
        status: int = None,
    ):
        # The list of extension points.
        self.bind_event_list = bind_event_list
        # The URL of the extension details page, on which users can view the details of the process blocked by the extension.
        self.detail_url = detail_url
        # The list of event types.
        self.event_category_list = event_category_list
        # The unique code of the extension.
        self.extension_code = extension_code
        # The description of the extension.
        self.extension_desc = extension_desc
        # The name of the extension.
        self.extension_name = extension_name
        # The URL of the help documentation of the extension.
        self.help_doc_url = help_doc_url
        # The options defined for the extension.
        self.option_setting = option_setting
        # The parameter settings of the extension. For more information, see [Configure extension parameters](https://help.aliyun.com/document_detail/405354.html).
        self.parameter_setting = parameter_setting
        # The workspace for testing. If the extension is being tested, the extension can be used only in the workspace for testing.
        self.project_testing = project_testing
        # The state of the extension. 0: Testing, 1: Publishing, 3: Disabled, 4: Processing, 5: Approved, 6: Approve Failed
        self.status = status

    def validate(self):
        if self.bind_event_list:
            for v1 in self.bind_event_list:
                 if v1:
                    v1.validate()
        if self.event_category_list:
            for v1 in self.event_category_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BindEventList'] = []
        if self.bind_event_list is not None:
            for k1 in self.bind_event_list:
                result['BindEventList'].append(k1.to_map() if k1 else None)

        if self.detail_url is not None:
            result['DetailUrl'] = self.detail_url

        result['EventCategoryList'] = []
        if self.event_category_list is not None:
            for k1 in self.event_category_list:
                result['EventCategoryList'].append(k1.to_map() if k1 else None)

        if self.extension_code is not None:
            result['ExtensionCode'] = self.extension_code

        if self.extension_desc is not None:
            result['ExtensionDesc'] = self.extension_desc

        if self.extension_name is not None:
            result['ExtensionName'] = self.extension_name

        if self.help_doc_url is not None:
            result['HelpDocUrl'] = self.help_doc_url

        if self.option_setting is not None:
            result['OptionSetting'] = self.option_setting

        if self.parameter_setting is not None:
            result['ParameterSetting'] = self.parameter_setting

        if self.project_testing is not None:
            result['ProjectTesting'] = self.project_testing

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bind_event_list = []
        if m.get('BindEventList') is not None:
            for k1 in m.get('BindEventList'):
                temp_model = main_models.GetExtensionResponseBodyExtensionBindEventList()
                self.bind_event_list.append(temp_model.from_map(k1))

        if m.get('DetailUrl') is not None:
            self.detail_url = m.get('DetailUrl')

        self.event_category_list = []
        if m.get('EventCategoryList') is not None:
            for k1 in m.get('EventCategoryList'):
                temp_model = main_models.GetExtensionResponseBodyExtensionEventCategoryList()
                self.event_category_list.append(temp_model.from_map(k1))

        if m.get('ExtensionCode') is not None:
            self.extension_code = m.get('ExtensionCode')

        if m.get('ExtensionDesc') is not None:
            self.extension_desc = m.get('ExtensionDesc')

        if m.get('ExtensionName') is not None:
            self.extension_name = m.get('ExtensionName')

        if m.get('HelpDocUrl') is not None:
            self.help_doc_url = m.get('HelpDocUrl')

        if m.get('OptionSetting') is not None:
            self.option_setting = m.get('OptionSetting')

        if m.get('ParameterSetting') is not None:
            self.parameter_setting = m.get('ParameterSetting')

        if m.get('ProjectTesting') is not None:
            self.project_testing = m.get('ProjectTesting')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetExtensionResponseBodyExtensionEventCategoryList(DaraModel):
    def __init__(
        self,
        category_code: str = None,
        category_name: str = None,
    ):
        # The code of the event type.
        self.category_code = category_code
        # The name of the event type.
        self.category_name = category_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_code is not None:
            result['CategoryCode'] = self.category_code

        if self.category_name is not None:
            result['CategoryName'] = self.category_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryCode') is not None:
            self.category_code = m.get('CategoryCode')

        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

        return self

class GetExtensionResponseBodyExtensionBindEventList(DaraModel):
    def __init__(
        self,
        event_code: str = None,
        event_name: str = None,
    ):
        # The code of the extension point event.
        self.event_code = event_code
        # The name of the extension point event.
        self.event_name = event_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_code is not None:
            result['EventCode'] = self.event_code

        if self.event_name is not None:
            result['EventName'] = self.event_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventCode') is not None:
            self.event_code = m.get('EventCode')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        return self

