# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alb20200616 import models as main_models
from darabonba.model import DaraModel

class CreateAScriptsRequest(DaraModel):
    def __init__(
        self,
        ascripts: List[main_models.CreateAScriptsRequestAScripts] = None,
        client_token: str = None,
        dry_run: bool = None,
        listener_id: str = None,
    ):
        # The information about the AScript rules.
        self.ascripts = ascripts
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false**(default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The listener ID.
        # 
        # This parameter is required.
        self.listener_id = listener_id

    def validate(self):
        if self.ascripts:
            for v1 in self.ascripts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AScripts'] = []
        if self.ascripts is not None:
            for k1 in self.ascripts:
                result['AScripts'].append(k1.to_map() if k1 else None)

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ascripts = []
        if m.get('AScripts') is not None:
            for k1 in m.get('AScripts'):
                temp_model = main_models.CreateAScriptsRequestAScripts()
                self.ascripts.append(temp_model.from_map(k1))

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        return self

class CreateAScriptsRequestAScripts(DaraModel):
    def __init__(
        self,
        ascript_name: str = None,
        enabled: bool = None,
        ext_attribute_enabled: bool = None,
        ext_attributes: List[main_models.CreateAScriptsRequestAScriptsExtAttributes] = None,
        position: str = None,
        script_content: str = None,
    ):
        # The name of the AScript rule.
        # 
        # The length must be between 2 and 128 characters. This name must start with a letter and can contain letters, digits, periods (.), underscores (_), and hyphens (-).
        # 
        # This parameter is required.
        self.ascript_name = ascript_name
        # Enables the AScript rule. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.enabled = enabled
        # Enables the extended attribute of the Ascript rule. Valid values:
        # 
        # *   true
        # *   false (default)
        self.ext_attribute_enabled = ext_attribute_enabled
        # The extended attribute of the AScript rule.
        self.ext_attributes = ext_attributes
        # The position where the Ascript rule is evaluated. Valid values are:
        # 
        # *   RequestHead (default): before inbound rules are evaluated
        # *   RequestFoot: after inbound rules are evaluated
        # *   ResponseHead: before outbound rules are evaluated
        self.position = position
        # The content of the AScript rule.
        # 
        # This parameter is required.
        self.script_content = script_content

    def validate(self):
        if self.ext_attributes:
            for v1 in self.ext_attributes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ascript_name is not None:
            result['AScriptName'] = self.ascript_name

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.ext_attribute_enabled is not None:
            result['ExtAttributeEnabled'] = self.ext_attribute_enabled

        result['ExtAttributes'] = []
        if self.ext_attributes is not None:
            for k1 in self.ext_attributes:
                result['ExtAttributes'].append(k1.to_map() if k1 else None)

        if self.position is not None:
            result['Position'] = self.position

        if self.script_content is not None:
            result['ScriptContent'] = self.script_content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AScriptName') is not None:
            self.ascript_name = m.get('AScriptName')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('ExtAttributeEnabled') is not None:
            self.ext_attribute_enabled = m.get('ExtAttributeEnabled')

        self.ext_attributes = []
        if m.get('ExtAttributes') is not None:
            for k1 in m.get('ExtAttributes'):
                temp_model = main_models.CreateAScriptsRequestAScriptsExtAttributes()
                self.ext_attributes.append(temp_model.from_map(k1))

        if m.get('Position') is not None:
            self.position = m.get('Position')

        if m.get('ScriptContent') is not None:
            self.script_content = m.get('ScriptContent')

        return self

class CreateAScriptsRequestAScriptsExtAttributes(DaraModel):
    def __init__(
        self,
        attribute_key: str = None,
        attribute_value: str = None,
    ):
        # The key of the extended attribute.
        # 
        # You can only set the key to **EsDebug**. This extended attribute adds a debug response header to record the execution of the AScript rule if the client request includes the _es_dbg parameter and its value matches the specified value of the extended attribute.
        self.attribute_key = attribute_key
        # The value of the extended attribute, which can contain a maximum of 128 characters, including letters and digits.
        self.attribute_value = attribute_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute_key is not None:
            result['AttributeKey'] = self.attribute_key

        if self.attribute_value is not None:
            result['AttributeValue'] = self.attribute_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeKey') is not None:
            self.attribute_key = m.get('AttributeKey')

        if m.get('AttributeValue') is not None:
            self.attribute_value = m.get('AttributeValue')

        return self

