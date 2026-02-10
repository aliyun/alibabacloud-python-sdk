# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetHoneypotPresetResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetHoneypotPresetResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code returned. The status code **200** indicates that the request was successful. Other status codes indicate that the request failed. You can identify the cause of the failure based on the status code.
        self.code = code
        # The information about the honeypot template.
        self.data = data
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The message returned.
        self.message = message
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

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
            temp_model = main_models.GetHoneypotPresetResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetHoneypotPresetResponseBodyData(DaraModel):
    def __init__(
        self,
        control_node_name: str = None,
        file_info_list: List[main_models.GetHoneypotPresetResponseBodyDataFileInfoList] = None,
        honeypot_image_display_name: str = None,
        honeypot_image_name: str = None,
        honeypot_preset_id: str = None,
        meta: str = None,
        node_id: str = None,
        preset_name: str = None,
        preset_type: str = None,
    ):
        # The name of the management node.
        self.control_node_name = control_node_name
        # An array that consists of the configurations of the uploaded file.
        self.file_info_list = file_info_list
        # The display name of the honeypot image.
        self.honeypot_image_display_name = honeypot_image_display_name
        # The name of the honeypot image.
        self.honeypot_image_name = honeypot_image_name
        # The ID of the honeypot template.
        self.honeypot_preset_id = honeypot_preset_id
        # The custom configuration of the honeypot template.
        self.meta = meta
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
        if self.file_info_list:
            for v1 in self.file_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.control_node_name is not None:
            result['ControlNodeName'] = self.control_node_name

        result['FileInfoList'] = []
        if self.file_info_list is not None:
            for k1 in self.file_info_list:
                result['FileInfoList'].append(k1.to_map() if k1 else None)

        if self.honeypot_image_display_name is not None:
            result['HoneypotImageDisplayName'] = self.honeypot_image_display_name

        if self.honeypot_image_name is not None:
            result['HoneypotImageName'] = self.honeypot_image_name

        if self.honeypot_preset_id is not None:
            result['HoneypotPresetId'] = self.honeypot_preset_id

        if self.meta is not None:
            result['Meta'] = self.meta

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

        self.file_info_list = []
        if m.get('FileInfoList') is not None:
            for k1 in m.get('FileInfoList'):
                temp_model = main_models.GetHoneypotPresetResponseBodyDataFileInfoList()
                self.file_info_list.append(temp_model.from_map(k1))

        if m.get('HoneypotImageDisplayName') is not None:
            self.honeypot_image_display_name = m.get('HoneypotImageDisplayName')

        if m.get('HoneypotImageName') is not None:
            self.honeypot_image_name = m.get('HoneypotImageName')

        if m.get('HoneypotPresetId') is not None:
            self.honeypot_preset_id = m.get('HoneypotPresetId')

        if m.get('Meta') is not None:
            self.meta = m.get('Meta')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('PresetName') is not None:
            self.preset_name = m.get('PresetName')

        if m.get('PresetType') is not None:
            self.preset_type = m.get('PresetType')

        return self

class GetHoneypotPresetResponseBodyDataFileInfoList(DaraModel):
    def __init__(
        self,
        file_id: str = None,
        file_name: str = None,
        oss_url: str = None,
    ):
        # The ID of the uploaded file.
        self.file_id = file_id
        # The name of the uploaded file.
        self.file_name = file_name
        # The download URL.
        self.oss_url = oss_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.oss_url is not None:
            result['OssUrl'] = self.oss_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('OssUrl') is not None:
            self.oss_url = m.get('OssUrl')

        return self

