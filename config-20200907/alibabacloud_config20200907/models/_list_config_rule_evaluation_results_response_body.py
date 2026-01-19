# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class ListConfigRuleEvaluationResultsResponseBody(DaraModel):
    def __init__(
        self,
        evaluation_results: main_models.ListConfigRuleEvaluationResultsResponseBodyEvaluationResults = None,
        request_id: str = None,
    ):
        # The compliance evaluation results returned.
        self.evaluation_results = evaluation_results
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.evaluation_results:
            self.evaluation_results.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.evaluation_results is not None:
            result['EvaluationResults'] = self.evaluation_results.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EvaluationResults') is not None:
            temp_model = main_models.ListConfigRuleEvaluationResultsResponseBodyEvaluationResults()
            self.evaluation_results = temp_model.from_map(m.get('EvaluationResults'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListConfigRuleEvaluationResultsResponseBodyEvaluationResults(DaraModel):
    def __init__(
        self,
        evaluation_result_list: List[main_models.ListConfigRuleEvaluationResultsResponseBodyEvaluationResultsEvaluationResultList] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The details of the compliance evaluation result.
        self.evaluation_result_list = evaluation_result_list
        # The maximum number of entries returned per page.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token

    def validate(self):
        if self.evaluation_result_list:
            for v1 in self.evaluation_result_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EvaluationResultList'] = []
        if self.evaluation_result_list is not None:
            for k1 in self.evaluation_result_list:
                result['EvaluationResultList'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.evaluation_result_list = []
        if m.get('EvaluationResultList') is not None:
            for k1 in m.get('EvaluationResultList'):
                temp_model = main_models.ListConfigRuleEvaluationResultsResponseBodyEvaluationResultsEvaluationResultList()
                self.evaluation_result_list.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

class ListConfigRuleEvaluationResultsResponseBodyEvaluationResultsEvaluationResultList(DaraModel):
    def __init__(
        self,
        annotation: str = None,
        compliance_type: str = None,
        config_rule_invoked_timestamp: int = None,
        evaluation_id: str = None,
        evaluation_result_identifier: main_models.ListConfigRuleEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifier = None,
        invoking_event_message_type: str = None,
        last_compliant_fixed_timestamp: int = None,
        last_non_compliant_record_timestamp: int = None,
        remediation_enabled: bool = None,
        result_recorded_timestamp: int = None,
        risk_level: int = None,
    ):
        # The annotation to the resource that is evaluated as non-compliant. The following section describe the parameters that can be returned:
        # 
        # *   `configuration`: the current resource configuration that is evaluated as non-compliant.
        # *   `desiredValue`: the expected resource configuration that is evaluated as compliant.
        # *   `operator`: the operator that compares the current configuration with the expected configuration of the resource.
        # *   `property`: the JSON path of the current configuration in the resource property struct.
        # *   `reason`: the reason why the resource is evaluated as non-compliant.
        self.annotation = annotation
        # The compliance evaluation result of the resource. Valid values:
        # 
        # *   COMPLIANT: The resources are evaluated as compliant.
        # *   NON_COMPLIANT: The resources are evaluated as non-compliant.
        # *   NOT_APPLICABLE: The rule does not apply to the resources.
        # *   INSUFFICIENT_DATA: No data is available.
        # *   IGNORED: The resource is ignored during compliance evaluation.
        self.compliance_type = compliance_type
        # The timestamp when the rule was triggered for the compliance evaluation. Unit: milliseconds.
        self.config_rule_invoked_timestamp = config_rule_invoked_timestamp
        self.evaluation_id = evaluation_id
        # The identifying information about the compliance evaluation result.
        self.evaluation_result_identifier = evaluation_result_identifier
        # The trigger type of the rule. Valid values:
        # 
        # *   ConfigurationItemChangeNotification: The rule is triggered by configuration changes.
        # *   ScheduledNotification: The rule is periodically triggered.
        # *   Manual: The rule is manually triggered.
        self.invoking_event_message_type = invoking_event_message_type
        self.last_compliant_fixed_timestamp = last_compliant_fixed_timestamp
        self.last_non_compliant_record_timestamp = last_non_compliant_record_timestamp
        # Indicates whether the remediation template is enabled. Valid values:
        # 
        # *   true: The remediation template is enabled.
        # *   false: The remediation template is disabled.
        self.remediation_enabled = remediation_enabled
        # The timestamp when the compliance evaluation result was recorded. Unit: milliseconds.
        self.result_recorded_timestamp = result_recorded_timestamp
        # The risk level of the resources that do not comply with the rule. Valid values:
        # 
        # *   1: high
        # *   2: medium
        # *   3: low
        self.risk_level = risk_level

    def validate(self):
        if self.evaluation_result_identifier:
            self.evaluation_result_identifier.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.annotation is not None:
            result['Annotation'] = self.annotation

        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type

        if self.config_rule_invoked_timestamp is not None:
            result['ConfigRuleInvokedTimestamp'] = self.config_rule_invoked_timestamp

        if self.evaluation_id is not None:
            result['EvaluationId'] = self.evaluation_id

        if self.evaluation_result_identifier is not None:
            result['EvaluationResultIdentifier'] = self.evaluation_result_identifier.to_map()

        if self.invoking_event_message_type is not None:
            result['InvokingEventMessageType'] = self.invoking_event_message_type

        if self.last_compliant_fixed_timestamp is not None:
            result['LastCompliantFixedTimestamp'] = self.last_compliant_fixed_timestamp

        if self.last_non_compliant_record_timestamp is not None:
            result['LastNonCompliantRecordTimestamp'] = self.last_non_compliant_record_timestamp

        if self.remediation_enabled is not None:
            result['RemediationEnabled'] = self.remediation_enabled

        if self.result_recorded_timestamp is not None:
            result['ResultRecordedTimestamp'] = self.result_recorded_timestamp

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Annotation') is not None:
            self.annotation = m.get('Annotation')

        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')

        if m.get('ConfigRuleInvokedTimestamp') is not None:
            self.config_rule_invoked_timestamp = m.get('ConfigRuleInvokedTimestamp')

        if m.get('EvaluationId') is not None:
            self.evaluation_id = m.get('EvaluationId')

        if m.get('EvaluationResultIdentifier') is not None:
            temp_model = main_models.ListConfigRuleEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifier()
            self.evaluation_result_identifier = temp_model.from_map(m.get('EvaluationResultIdentifier'))

        if m.get('InvokingEventMessageType') is not None:
            self.invoking_event_message_type = m.get('InvokingEventMessageType')

        if m.get('LastCompliantFixedTimestamp') is not None:
            self.last_compliant_fixed_timestamp = m.get('LastCompliantFixedTimestamp')

        if m.get('LastNonCompliantRecordTimestamp') is not None:
            self.last_non_compliant_record_timestamp = m.get('LastNonCompliantRecordTimestamp')

        if m.get('RemediationEnabled') is not None:
            self.remediation_enabled = m.get('RemediationEnabled')

        if m.get('ResultRecordedTimestamp') is not None:
            self.result_recorded_timestamp = m.get('ResultRecordedTimestamp')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        return self

class ListConfigRuleEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifier(DaraModel):
    def __init__(
        self,
        evaluation_result_qualifier: main_models.ListConfigRuleEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifierEvaluationResultQualifier = None,
        ordering_timestamp: int = None,
    ):
        # The information about the evaluated resource in the compliance evaluation result.
        self.evaluation_result_qualifier = evaluation_result_qualifier
        # The timestamp when the compliance evaluation was performed. Unit: milliseconds.
        self.ordering_timestamp = ordering_timestamp

    def validate(self):
        if self.evaluation_result_qualifier:
            self.evaluation_result_qualifier.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.evaluation_result_qualifier is not None:
            result['EvaluationResultQualifier'] = self.evaluation_result_qualifier.to_map()

        if self.ordering_timestamp is not None:
            result['OrderingTimestamp'] = self.ordering_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EvaluationResultQualifier') is not None:
            temp_model = main_models.ListConfigRuleEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifierEvaluationResultQualifier()
            self.evaluation_result_qualifier = temp_model.from_map(m.get('EvaluationResultQualifier'))

        if m.get('OrderingTimestamp') is not None:
            self.ordering_timestamp = m.get('OrderingTimestamp')

        return self

class ListConfigRuleEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifierEvaluationResultQualifier(DaraModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        config_rule_arn: str = None,
        config_rule_id: str = None,
        config_rule_name: str = None,
        ignore_date: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
    ):
        # The ID of the compliance package to which the rule belongs.
        self.compliance_pack_id = compliance_pack_id
        # The ARN of the rule.
        self.config_rule_arn = config_rule_arn
        # The rule ID.
        self.config_rule_id = config_rule_id
        # The rule name.
        self.config_rule_name = config_rule_name
        # The date on which the system automatically re-evaluates the ignored incompliant resources.
        # 
        # >  If the value of this parameter is left empty, the system does not automatically re-evaluate the ignored incompliant resources. You must manually re-evaluate the ignored incompliant resources.
        self.ignore_date = ignore_date
        # The ID of the region in which your resources reside.
        self.region_id = region_id
        # This parameter is required.
        self.resource_group_id = resource_group_id
        # The resource ID.
        self.resource_id = resource_id
        # The resource name.
        self.resource_name = resource_name
        # The ID of the Alibaba Cloud account to which the resource belongs.
        self.resource_owner_id = resource_owner_id
        # The type of the resource that is monitored by Cloud Config.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id

        if self.config_rule_arn is not None:
            result['ConfigRuleArn'] = self.config_rule_arn

        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id

        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name

        if self.ignore_date is not None:
            result['IgnoreDate'] = self.ignore_date

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')

        if m.get('ConfigRuleArn') is not None:
            self.config_rule_arn = m.get('ConfigRuleArn')

        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')

        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')

        if m.get('IgnoreDate') is not None:
            self.ignore_date = m.get('IgnoreDate')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

