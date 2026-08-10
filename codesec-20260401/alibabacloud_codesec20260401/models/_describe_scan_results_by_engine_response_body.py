# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_codesec20260401 import models as main_models
from darabonba.model import DaraModel

class DescribeScanResultsByEngineResponseBody(DaraModel):
    def __init__(
        self,
        engine: str = None,
        items: List[main_models.DescribeScanResultsByEngineResponseBodyItems] = None,
        max_results: int = None,
        next_token: str = None,
        project_id: int = None,
        request_id: str = None,
        scan_id: int = None,
        total_count: int = None,
    ):
        self.engine = engine
        self.items = items
        self.max_results = max_results
        self.next_token = next_token
        self.project_id = project_id
        self.request_id = request_id
        self.scan_id = scan_id
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.engine is not None:
            result['engine'] = self.engine

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.project_id is not None:
            result['projectId'] = self.project_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.scan_id is not None:
            result['scanId'] = self.scan_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('engine') is not None:
            self.engine = m.get('engine')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.DescribeScanResultsByEngineResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('scanId') is not None:
            self.scan_id = m.get('scanId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class DescribeScanResultsByEngineResponseBodyItems(DaraModel):
    def __init__(
        self,
        baseline_state: str = None,
        category: str = None,
        code_snippet: str = None,
        confidence: float = None,
        created_at: str = None,
        cwe_id: str = None,
        description: str = None,
        end_line: int = None,
        file_path: str = None,
        id: int = None,
        item_summary: str = None,
        owasp_category: str = None,
        project_name: str = None,
        remediation_code_example: str = None,
        remediation_suggestion: str = None,
        rule_id: str = None,
        sca_component: main_models.DescribeScanResultsByEngineResponseBodyItemsScaComponent = None,
        scan_id: int = None,
        severity: str = None,
        source: str = None,
        start_line: int = None,
        status: str = None,
        taint_flow: List[main_models.DescribeScanResultsByEngineResponseBodyItemsTaintFlow] = None,
        taint_flow_summary: str = None,
        title: str = None,
    ):
        self.baseline_state = baseline_state
        self.category = category
        self.code_snippet = code_snippet
        self.confidence = confidence
        # 发现记录创建时间（RFC3339）
        self.created_at = created_at
        self.cwe_id = cwe_id
        self.description = description
        self.end_line = end_line
        self.file_path = file_path
        self.id = id
        self.item_summary = item_summary
        self.owasp_category = owasp_category
        self.project_name = project_name
        self.remediation_code_example = remediation_code_example
        self.remediation_suggestion = remediation_suggestion
        self.rule_id = rule_id
        self.sca_component = sca_component
        self.scan_id = scan_id
        self.severity = severity
        self.source = source
        self.start_line = start_line
        self.status = status
        self.taint_flow = taint_flow
        self.taint_flow_summary = taint_flow_summary
        self.title = title

    def validate(self):
        if self.sca_component:
            self.sca_component.validate()
        if self.taint_flow:
            for v1 in self.taint_flow:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baseline_state is not None:
            result['baselineState'] = self.baseline_state

        if self.category is not None:
            result['category'] = self.category

        if self.code_snippet is not None:
            result['codeSnippet'] = self.code_snippet

        if self.confidence is not None:
            result['confidence'] = self.confidence

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.cwe_id is not None:
            result['cweId'] = self.cwe_id

        if self.description is not None:
            result['description'] = self.description

        if self.end_line is not None:
            result['endLine'] = self.end_line

        if self.file_path is not None:
            result['filePath'] = self.file_path

        if self.id is not None:
            result['id'] = self.id

        if self.item_summary is not None:
            result['itemSummary'] = self.item_summary

        if self.owasp_category is not None:
            result['owaspCategory'] = self.owasp_category

        if self.project_name is not None:
            result['projectName'] = self.project_name

        if self.remediation_code_example is not None:
            result['remediationCodeExample'] = self.remediation_code_example

        if self.remediation_suggestion is not None:
            result['remediationSuggestion'] = self.remediation_suggestion

        if self.rule_id is not None:
            result['ruleId'] = self.rule_id

        if self.sca_component is not None:
            result['scaComponent'] = self.sca_component.to_map()

        if self.scan_id is not None:
            result['scanId'] = self.scan_id

        if self.severity is not None:
            result['severity'] = self.severity

        if self.source is not None:
            result['source'] = self.source

        if self.start_line is not None:
            result['startLine'] = self.start_line

        if self.status is not None:
            result['status'] = self.status

        result['taintFlow'] = []
        if self.taint_flow is not None:
            for k1 in self.taint_flow:
                result['taintFlow'].append(k1.to_map() if k1 else None)

        if self.taint_flow_summary is not None:
            result['taintFlowSummary'] = self.taint_flow_summary

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('baselineState') is not None:
            self.baseline_state = m.get('baselineState')

        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('codeSnippet') is not None:
            self.code_snippet = m.get('codeSnippet')

        if m.get('confidence') is not None:
            self.confidence = m.get('confidence')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('cweId') is not None:
            self.cwe_id = m.get('cweId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('endLine') is not None:
            self.end_line = m.get('endLine')

        if m.get('filePath') is not None:
            self.file_path = m.get('filePath')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('itemSummary') is not None:
            self.item_summary = m.get('itemSummary')

        if m.get('owaspCategory') is not None:
            self.owasp_category = m.get('owaspCategory')

        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')

        if m.get('remediationCodeExample') is not None:
            self.remediation_code_example = m.get('remediationCodeExample')

        if m.get('remediationSuggestion') is not None:
            self.remediation_suggestion = m.get('remediationSuggestion')

        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')

        if m.get('scaComponent') is not None:
            temp_model = main_models.DescribeScanResultsByEngineResponseBodyItemsScaComponent()
            self.sca_component = temp_model.from_map(m.get('scaComponent'))

        if m.get('scanId') is not None:
            self.scan_id = m.get('scanId')

        if m.get('severity') is not None:
            self.severity = m.get('severity')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('startLine') is not None:
            self.start_line = m.get('startLine')

        if m.get('status') is not None:
            self.status = m.get('status')

        self.taint_flow = []
        if m.get('taintFlow') is not None:
            for k1 in m.get('taintFlow'):
                temp_model = main_models.DescribeScanResultsByEngineResponseBodyItemsTaintFlow()
                self.taint_flow.append(temp_model.from_map(k1))

        if m.get('taintFlowSummary') is not None:
            self.taint_flow_summary = m.get('taintFlowSummary')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class DescribeScanResultsByEngineResponseBodyItemsTaintFlow(DaraModel):
    def __init__(
        self,
        code: str = None,
        file: str = None,
        kind: str = None,
        line: int = None,
        note: str = None,
        step: int = None,
    ):
        self.code = code
        self.file = file
        self.kind = kind
        self.line = line
        self.note = note
        self.step = step

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.file is not None:
            result['file'] = self.file

        if self.kind is not None:
            result['kind'] = self.kind

        if self.line is not None:
            result['line'] = self.line

        if self.note is not None:
            result['note'] = self.note

        if self.step is not None:
            result['step'] = self.step

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('file') is not None:
            self.file = m.get('file')

        if m.get('kind') is not None:
            self.kind = m.get('kind')

        if m.get('line') is not None:
            self.line = m.get('line')

        if m.get('note') is not None:
            self.note = m.get('note')

        if m.get('step') is not None:
            self.step = m.get('step')

        return self

class DescribeScanResultsByEngineResponseBodyItemsScaComponent(DaraModel):
    def __init__(
        self,
        cve_count: int = None,
        cve_details: List[main_models.DescribeScanResultsByEngineResponseBodyItemsScaComponentCveDetails] = None,
        intro_paths: List[str] = None,
        is_direct: bool = None,
        package_name: str = None,
        remediation: str = None,
        version: str = None,
    ):
        self.cve_count = cve_count
        self.cve_details = cve_details
        self.intro_paths = intro_paths
        self.is_direct = is_direct
        self.package_name = package_name
        self.remediation = remediation
        self.version = version

    def validate(self):
        if self.cve_details:
            for v1 in self.cve_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cve_count is not None:
            result['cveCount'] = self.cve_count

        result['cveDetails'] = []
        if self.cve_details is not None:
            for k1 in self.cve_details:
                result['cveDetails'].append(k1.to_map() if k1 else None)

        if self.intro_paths is not None:
            result['introPaths'] = self.intro_paths

        if self.is_direct is not None:
            result['isDirect'] = self.is_direct

        if self.package_name is not None:
            result['packageName'] = self.package_name

        if self.remediation is not None:
            result['remediation'] = self.remediation

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cveCount') is not None:
            self.cve_count = m.get('cveCount')

        self.cve_details = []
        if m.get('cveDetails') is not None:
            for k1 in m.get('cveDetails'):
                temp_model = main_models.DescribeScanResultsByEngineResponseBodyItemsScaComponentCveDetails()
                self.cve_details.append(temp_model.from_map(k1))

        if m.get('introPaths') is not None:
            self.intro_paths = m.get('introPaths')

        if m.get('isDirect') is not None:
            self.is_direct = m.get('isDirect')

        if m.get('packageName') is not None:
            self.package_name = m.get('packageName')

        if m.get('remediation') is not None:
            self.remediation = m.get('remediation')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class DescribeScanResultsByEngineResponseBodyItemsScaComponentCveDetails(DaraModel):
    def __init__(
        self,
        cve_id: str = None,
        cvss: float = None,
        cvss_version: str = None,
        description: str = None,
        references: List[str] = None,
        severity: str = None,
    ):
        self.cve_id = cve_id
        self.cvss = cvss
        self.cvss_version = cvss_version
        self.description = description
        self.references = references
        self.severity = severity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cve_id is not None:
            result['cveId'] = self.cve_id

        if self.cvss is not None:
            result['cvss'] = self.cvss

        if self.cvss_version is not None:
            result['cvssVersion'] = self.cvss_version

        if self.description is not None:
            result['description'] = self.description

        if self.references is not None:
            result['references'] = self.references

        if self.severity is not None:
            result['severity'] = self.severity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cveId') is not None:
            self.cve_id = m.get('cveId')

        if m.get('cvss') is not None:
            self.cvss = m.get('cvss')

        if m.get('cvssVersion') is not None:
            self.cvss_version = m.get('cvssVersion')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('references') is not None:
            self.references = m.get('references')

        if m.get('severity') is not None:
            self.severity = m.get('severity')

        return self

