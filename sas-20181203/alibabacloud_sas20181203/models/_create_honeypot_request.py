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
        # The ID of the honeypot image.
        # 
        # > You can call the [ListAvailableHoneypot](~~ListAvailableHoneypot~~) operation to query the IDs of images from the **HoneypotImageId** response parameter.
        # 
        # This parameter is required.
        self.honeypot_image_id = honeypot_image_id
        # The name of the honeypot image.
        # 
        # > You can call the [ListAvailableHoneypot](~~ListAvailableHoneypot~~) operation to query the names of images from the **HoneypotImageName** response parameter.
        # 
        # This parameter is required.
        self.honeypot_image_name = honeypot_image_name
        # The custom name of the honeypot.
        # 
        # This parameter is required.
        self.honeypot_name = honeypot_name
        # The custom configuration of the honeypot in the JSON format. The value contains the following fields:
        # 
        # *   **trojan_git**: Git-specific Defense. Valid values:
        # 
        #     *   **zip**: Git Source Code Package
        #     *   **web**: Git Directory Leak
        #     *   **close**: Disabled
        # 
        # *   **trojan_git_addr**: Git Trojan Address.
        # 
        # *   **trojan_git.zip**: Git Trojan.
        # 
        # *   **burp**: Burp-specific Defense. Valid values:
        # 
        #     *   **open**: Enable
        #     *   **close**: Disable
        # 
        # *   **portrait_option**: Source Tracing Configuration. Valid values:
        # 
        #     *   **false**: Disable
        #     *   **true**: Enable
        self.meta = meta
        # The ID of the management node.
        # 
        # > You can call the [ListHoneypotNode](~~ListHoneypotNode~~) operation to query the IDs of management nodes.
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

