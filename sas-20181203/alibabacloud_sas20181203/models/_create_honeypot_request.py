# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateHoneypotRequest(DaraModel):
    def __init__(
        self,
        honeypot_image_id: str = None,
        honeypot_image_name: str = None,
        honeypot_name: str = None,
        meta: str = None,
        node_id: str = None,
    ):
        # The honeypot image ID.
        # > You can obtain this value from the **HoneypotImageId** field returned by the [ListAvailableHoneypot](~~ListAvailableHoneypot~~) operation.
        # 
        # This parameter is required.
        self.honeypot_image_id = honeypot_image_id
        # The honeypot image name.
        # > You can obtain this value from the **HoneypotImageName** field returned by the [ListAvailableHoneypot](~~ListAvailableHoneypot~~) operation.
        # 
        # This parameter is required.
        self.honeypot_image_name = honeypot_image_name
        # The custom name of the honeypot.
        # 
        # This parameter is required.
        self.honeypot_name = honeypot_name
        # The custom configuration of the honeypot in JSON format. The following fields are included:
        # 
        # - **trojan_git**: The Git counter-intelligence method. Valid values:
        #     -   **zip**: Git source code package.
        #     -  **web**: .git folder leak.
        #     -  **close**: Shutdown.
        # - **trojan_git_addr**: The Git counter-intelligence endpoint.
        # - **trojan_git.zip**: The Git counter-intelligence trojan package.
        # - **burp**: The Burp counter-intelligence method. Valid values:
        #      - **open**: Enabled.
        #     - **close**: Shutdown.
        # - **portrait_option**: The tracing configuration. Valid values:
        #     - **false**: Shutdown.
        #     - **true**: Enabled.
        self.meta = meta
        # The ID of the honeypot management node.
        # > Call the [ListHoneypotNode](~~ListHoneypotNode~~) operation to obtain this value.
        # 
        # This parameter is required.
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.honeypot_image_id is not None:
            result['HoneypotImageId'] = self.honeypot_image_id

        if self.honeypot_image_name is not None:
            result['HoneypotImageName'] = self.honeypot_image_name

        if self.honeypot_name is not None:
            result['HoneypotName'] = self.honeypot_name

        if self.meta is not None:
            result['Meta'] = self.meta

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HoneypotImageId') is not None:
            self.honeypot_image_id = m.get('HoneypotImageId')

        if m.get('HoneypotImageName') is not None:
            self.honeypot_image_name = m.get('HoneypotImageName')

        if m.get('HoneypotName') is not None:
            self.honeypot_name = m.get('HoneypotName')

        if m.get('Meta') is not None:
            self.meta = m.get('Meta')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        return self

