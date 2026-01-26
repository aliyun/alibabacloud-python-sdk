# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateIntegrationRequest(DaraModel):
    def __init__(
        self,
        auto_recover: bool = None,
        description: str = None,
        duplicate_key: str = None,
        extended_field_redefine_rules: str = None,
        field_redefine_rules: str = None,
        initiative_recover_field: str = None,
        initiative_recover_value: str = None,
        integration_id: int = None,
        integration_name: str = None,
        integration_product_type: str = None,
        liveness: str = None,
        recover_time: int = None,
        stat: str = None,
        state: bool = None,
    ):
        # Specifies whether to automatically clear alert events. Valid values:
        # 
        # *   true (default)
        # *   false
        self.auto_recover = auto_recover
        # The description of the alert integration.
        self.description = description
        # The fields whose values are deduplicated.
        self.duplicate_key = duplicate_key
        # The extended mapped fields are mapped to the fields of ARMS alerts. For more information, see the description of the ExtendedFieldRedefineRules parameter.
        self.extended_field_redefine_rules = extended_field_redefine_rules
        # The predefined mapped fields are mapped to the fields of ARMS alerts. The predefined mapped fields were generated when the alert integration was created. For more information, see the description of the FieldRedefineRules parameter.
        self.field_redefine_rules = field_redefine_rules
        # The field for clearing alert events. The system queries alert events based on the field of alert clearing events and clears the alert events.
        # 
        # > Only the Log Service alert integration supports the parameter.
        self.initiative_recover_field = initiative_recover_field
        # The value of the field for clearing alert events. The system queries alert events based on the field of alert clearing events and clears the alert events.
        # 
        # > Only the Log Service alert integration supports the parameter.
        self.initiative_recover_value = initiative_recover_value
        # The ID of the alert integration.
        # 
        # This parameter is required.
        self.integration_id = integration_id
        # The name of the alert integration.
        # 
        # This parameter is required.
        self.integration_name = integration_name
        # The service of the alert integration. Valid values:
        # 
        # *   CLOUD_MONITOR: CloudMonitor
        # *   LOG_SERVICE: Log Service
        # 
        # This parameter is required.
        self.integration_product_type = integration_product_type
        # The activity of the alert integration
        self.liveness = liveness
        # The period of time within which alert events are automatically cleared. Unit: seconds. Default value: 300.
        self.recover_time = recover_time
        # The total number of alert events and the number of abnormal alert events in the last hour.
        self.stat = stat
        # Indicates whether the alert integration was enabled. Valid values:
        # 
        # *   true
        # *   false
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_recover is not None:
            result['AutoRecover'] = self.auto_recover

        if self.description is not None:
            result['Description'] = self.description

        if self.duplicate_key is not None:
            result['DuplicateKey'] = self.duplicate_key

        if self.extended_field_redefine_rules is not None:
            result['ExtendedFieldRedefineRules'] = self.extended_field_redefine_rules

        if self.field_redefine_rules is not None:
            result['FieldRedefineRules'] = self.field_redefine_rules

        if self.initiative_recover_field is not None:
            result['InitiativeRecoverField'] = self.initiative_recover_field

        if self.initiative_recover_value is not None:
            result['InitiativeRecoverValue'] = self.initiative_recover_value

        if self.integration_id is not None:
            result['IntegrationId'] = self.integration_id

        if self.integration_name is not None:
            result['IntegrationName'] = self.integration_name

        if self.integration_product_type is not None:
            result['IntegrationProductType'] = self.integration_product_type

        if self.liveness is not None:
            result['Liveness'] = self.liveness

        if self.recover_time is not None:
            result['RecoverTime'] = self.recover_time

        if self.stat is not None:
            result['Stat'] = self.stat

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRecover') is not None:
            self.auto_recover = m.get('AutoRecover')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DuplicateKey') is not None:
            self.duplicate_key = m.get('DuplicateKey')

        if m.get('ExtendedFieldRedefineRules') is not None:
            self.extended_field_redefine_rules = m.get('ExtendedFieldRedefineRules')

        if m.get('FieldRedefineRules') is not None:
            self.field_redefine_rules = m.get('FieldRedefineRules')

        if m.get('InitiativeRecoverField') is not None:
            self.initiative_recover_field = m.get('InitiativeRecoverField')

        if m.get('InitiativeRecoverValue') is not None:
            self.initiative_recover_value = m.get('InitiativeRecoverValue')

        if m.get('IntegrationId') is not None:
            self.integration_id = m.get('IntegrationId')

        if m.get('IntegrationName') is not None:
            self.integration_name = m.get('IntegrationName')

        if m.get('IntegrationProductType') is not None:
            self.integration_product_type = m.get('IntegrationProductType')

        if m.get('Liveness') is not None:
            self.liveness = m.get('Liveness')

        if m.get('RecoverTime') is not None:
            self.recover_time = m.get('RecoverTime')

        if m.get('Stat') is not None:
            self.stat = m.get('Stat')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

