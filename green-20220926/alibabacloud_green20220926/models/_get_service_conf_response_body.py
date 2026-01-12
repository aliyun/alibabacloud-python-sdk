# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class GetServiceConfResponseBody(DaraModel):
    def __init__(
        self,
        classify: str = None,
        code: int = None,
        custom_service_conf: Dict[str, Any] = None,
        gmt_modified: str = None,
        msg: str = None,
        option: Dict[str, Any] = None,
        request_id: str = None,
        resource_type: str = None,
        service_code: str = None,
        service_type: str = None,
        success: bool = None,
        uid: str = None,
    ):
        # Classification.
        self.classify = classify
        # Error code, consistent with HTTP status.
        self.code = code
        # Service details
        self.custom_service_conf = custom_service_conf
        # Modification time.
        self.gmt_modified = gmt_modified
        # Further description of the error code.
        self.msg = msg
        # Options.
        self.option = option
        # ID assigned by the backend to uniquely identify a request. Can be used for troubleshooting.
        self.request_id = request_id
        # Resource type.
        self.resource_type = resource_type
        # Service code.
        self.service_code = service_code
        # Service type.
        self.service_type = service_type
        # Success indicator
        self.success = success
        # UID.
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.classify is not None:
            result['Classify'] = self.classify

        if self.code is not None:
            result['Code'] = self.code

        if self.custom_service_conf is not None:
            result['CustomServiceConf'] = self.custom_service_conf

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.option is not None:
            result['Option'] = self.option

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.service_code is not None:
            result['ServiceCode'] = self.service_code

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        if self.success is not None:
            result['Success'] = self.success

        if self.uid is not None:
            result['Uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Classify') is not None:
            self.classify = m.get('Classify')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CustomServiceConf') is not None:
            self.custom_service_conf = m.get('CustomServiceConf')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('Option') is not None:
            self.option = m.get('Option')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

