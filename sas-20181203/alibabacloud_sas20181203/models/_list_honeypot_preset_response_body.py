# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListHoneypotPresetResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        list: List[main_models.ListHoneypotPresetResponseBodyList] = None,
        message: str = None,
        page_info: main_models.ListHoneypotPresetResponseBodyPageInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code returned. The status code **200** indicates that the request was successful. Other status codes indicate that the request failed. You can identify the cause of the failure based on the status code.
        self.code = code
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # An array that consists of the honeypot templates.
        self.list = list
        # The message returned.
        self.message = message
        # The pagination information.
        self.page_info = page_info
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.ListHoneypotPresetResponseBodyList()
                self.list.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListHoneypotPresetResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListHoneypotPresetResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page. Default value: 20.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListHoneypotPresetResponseBodyList(DaraModel):
    def __init__(
        self,
        control_node_name: str = None,
        honeypot_image_display_name: str = None,
        honeypot_image_name: str = None,
        honeypot_preset_id: str = None,
        node_id: str = None,
        preset_name: str = None,
        preset_type: str = None,
    ):
        # The name of the management node.
        self.control_node_name = control_node_name
        # The display name of the honeypot image.
        self.honeypot_image_display_name = honeypot_image_display_name
        # The name of the honeypot image.
        self.honeypot_image_name = honeypot_image_name
        # The ID of the honeypot template.
        self.honeypot_preset_id = honeypot_preset_id
        # The ID of the management node.
        self.node_id = node_id
        # The custom name of the honeypot template.
        self.preset_name = preset_name
        # The type of the honeypot template. Valid values:
        # 
        # *   **TEMP**: automatically generated template
        # *   **CUSTOM**: custom template
        # *   **DEFAULT**: default template
        self.preset_type = preset_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.control_node_name is not None:
            result['ControlNodeName'] = self.control_node_name

        if self.honeypot_image_display_name is not None:
            result['HoneypotImageDisplayName'] = self.honeypot_image_display_name

        if self.honeypot_image_name is not None:
            result['HoneypotImageName'] = self.honeypot_image_name

        if self.honeypot_preset_id is not None:
            result['HoneypotPresetId'] = self.honeypot_preset_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.preset_name is not None:
            result['PresetName'] = self.preset_name

        if self.preset_type is not None:
            result['PresetType'] = self.preset_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ControlNodeName') is not None:
            self.control_node_name = m.get('ControlNodeName')

        if m.get('HoneypotImageDisplayName') is not None:
            self.honeypot_image_display_name = m.get('HoneypotImageDisplayName')

        if m.get('HoneypotImageName') is not None:
            self.honeypot_image_name = m.get('HoneypotImageName')

        if m.get('HoneypotPresetId') is not None:
            self.honeypot_preset_id = m.get('HoneypotPresetId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('PresetName') is not None:
            self.preset_name = m.get('PresetName')

        if m.get('PresetType') is not None:
            self.preset_type = m.get('PresetType')

        return self

