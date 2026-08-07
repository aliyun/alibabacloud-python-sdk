# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class GetAppConfigResponseBody(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        classify: str = None,
        custom_config: Dict[str, Any] = None,
        deploy_status: str = None,
        gmt_modified: str = None,
        name: str = None,
        option: Dict[str, Any] = None,
        request_id: str = None,
        resource_type: str = None,
        type: str = None,
        version: int = None,
    ):
        # App ID。
        self.app_id = app_id
        # The category.
        self.classify = classify
        # The configuration details.
        self.custom_config = custom_config
        # The publish status.
        self.deploy_status = deploy_status
        # The modification time.
        self.gmt_modified = gmt_modified
        # The application name.
        self.name = name
        # The preset options.
        self.option = option
        # The ID assigned by the backend to uniquely identify a request. This ID can be used to troubleshoot issues.
        self.request_id = request_id
        # The resource type.
        self.resource_type = resource_type
        # The type.
        self.type = type
        # The version number.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.classify is not None:
            result['Classify'] = self.classify

        if self.custom_config is not None:
            result['CustomConfig'] = self.custom_config

        if self.deploy_status is not None:
            result['DeployStatus'] = self.deploy_status

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.name is not None:
            result['Name'] = self.name

        if self.option is not None:
            result['Option'] = self.option

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.type is not None:
            result['Type'] = self.type

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Classify') is not None:
            self.classify = m.get('Classify')

        if m.get('CustomConfig') is not None:
            self.custom_config = m.get('CustomConfig')

        if m.get('DeployStatus') is not None:
            self.deploy_status = m.get('DeployStatus')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Option') is not None:
            self.option = m.get('Option')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

