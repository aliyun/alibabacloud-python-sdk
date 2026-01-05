# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alb20200616 import models as main_models
from darabonba.model import DaraModel

class UpdateAScriptsRequest(DaraModel):
    def __init__(
        self,
        ascripts: List[main_models.UpdateAScriptsRequestAScripts] = None,
        client_token: str = None,
        dry_run: bool = None,
    ):
        # The information about the AScript rule.
        self.ascripts = ascripts
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false**(default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ascripts = []
        if m.get('AScripts') is not None:
            for k1 in m.get('AScripts'):
                temp_model = main_models.UpdateAScriptsRequestAScripts()
                self.ascripts.append(temp_model.from_map(k1))

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        return self

class UpdateAScriptsRequestAScripts(DaraModel):
    def __init__(
        self,
        ascript_id: str = None,
        ascript_name: str = None,
        enabled: bool = None,
        ext_attribute_enabled: bool = None,
        ext_attributes: List[main_models.UpdateAScriptsRequestAScriptsExtAttributes] = None,
        script_content: str = None,
    ):
        # The rule ID.
        # 
        # This parameter is required.
        self.ascript_id = ascript_id
        # The name of the AScript rule.
        # 
        # The name must be 2 to 128 character in length, and can contain letters, digits, periods (.), underscores (_), and hyphens (-). It must start with a letter.
        self.ascript_name = ascript_name
        # Specifies whether to enable the AScript rule. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.enabled = enabled
        # Specifies whether to enable the extended attributes of the Ascript rule. Valid values:
        # 
        # *   true
        # *   false (false)
        self.ext_attribute_enabled = ext_attribute_enabled
        # The extended attribute.
        self.ext_attributes = ext_attributes
        # The content of the AScript rule.
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
        if self.ascript_id is not None:
            result['AScriptId'] = self.ascript_id

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

        if self.script_content is not None:
            result['ScriptContent'] = self.script_content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AScriptId') is not None:
            self.ascript_id = m.get('AScriptId')

        if m.get('AScriptName') is not None:
            self.ascript_name = m.get('AScriptName')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('ExtAttributeEnabled') is not None:
            self.ext_attribute_enabled = m.get('ExtAttributeEnabled')

        self.ext_attributes = []
        if m.get('ExtAttributes') is not None:
            for k1 in m.get('ExtAttributes'):
                temp_model = main_models.UpdateAScriptsRequestAScriptsExtAttributes()
                self.ext_attributes.append(temp_model.from_map(k1))

        if m.get('ScriptContent') is not None:
            self.script_content = m.get('ScriptContent')

        return self

class UpdateAScriptsRequestAScriptsExtAttributes(DaraModel):
    def __init__(
        self,
        attribute_key: str = None,
        attribute_value: str = None,
    ):
        # The attribute name.
        # 
        # Set the value to **EsDebug**, which specifies that when requests carry the _es_dbg parameter whose value is the specified key, the debugging header is enabled to output the execution result.
        # 
        # This parameter is required.
        self.attribute_key = attribute_key
        # The attribute value, which must be 1 to 128 characters in length, and can contain letters and digits.
        # 
        # This parameter is required.
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

