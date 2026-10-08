# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSlsLogStoreRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        configs: str = None,
    ):
        # The ID of the application. You can call the ListApplication operation to query the application ID. For more information, see [ListApplication](https://help.aliyun.com/document_detail/149390.html).
        # 
        # This parameter is required.
        self.app_id = app_id
        # The configurations of the Logstore.
        # 
        # *   The following parameters are included in the configurations:****
        # 
        #     *   **type**: the collection type. Set this parameter to file to specify the file type. Set this parameter to stdout to specify the standard output type.
        # 
        #     *   **logstore**: the name of the Logstore. Make sure that the name of the Logstore is unique in the cluster. The name must comply with the following rules:
        # 
        #         *   The name can contain only lowercase letters, digits, hyphens (-), and underscores (_).
        #         *   The name must start and end with a lowercase letter or a digit.
        #         *   The name must be 3 to 63 characters in length.
        # 
        #         **
        # 
        #         **Note**If you leave this parameter empty, the system automatically generates a name.
        # 
        #     *   **LogDir**: If the standard output type is used, the collection path is stdout.log. If the file type is used, the collection path is the path of the collected file. Wildcards (\\*) are supported. The collection path must match the following regular expression: `^/(.+)/(.*)^/$`.
        # 
        # This parameter is required.
        self.configs = configs

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.configs is not None:
            result['Configs'] = self.configs

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Configs') is not None:
            self.configs = m.get('Configs')

        return self

