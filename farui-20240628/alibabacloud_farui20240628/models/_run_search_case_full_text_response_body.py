# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_farui20240628 import models as main_models
from darabonba.model import DaraModel

class RunSearchCaseFullTextResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.RunSearchCaseFullTextResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.RunSearchCaseFullTextResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class RunSearchCaseFullTextResponseBodyData(DaraModel):
    def __init__(
        self,
        case_level: str = None,
        case_result: List[main_models.RunSearchCaseFullTextResponseBodyDataCaseResult] = None,
        current_page: int = None,
        page_size: int = None,
        query: str = None,
        query_keywords: List[str] = None,
        total_count: int = None,
    ):
        self.case_level = case_level
        self.case_result = case_result
        self.current_page = current_page
        self.page_size = page_size
        self.query = query
        self.query_keywords = query_keywords
        self.total_count = total_count

    def validate(self):
        if self.case_result:
            for v1 in self.case_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.case_level is not None:
            result['caseLevel'] = self.case_level

        result['caseResult'] = []
        if self.case_result is not None:
            for k1 in self.case_result:
                result['caseResult'].append(k1.to_map() if k1 else None)

        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.query is not None:
            result['query'] = self.query

        if self.query_keywords is not None:
            result['queryKeywords'] = self.query_keywords

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('caseLevel') is not None:
            self.case_level = m.get('caseLevel')

        self.case_result = []
        if m.get('caseResult') is not None:
            for k1 in m.get('caseResult'):
                temp_model = main_models.RunSearchCaseFullTextResponseBodyDataCaseResult()
                self.case_result.append(temp_model.from_map(k1))

        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('queryKeywords') is not None:
            self.query_keywords = m.get('queryKeywords')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class RunSearchCaseFullTextResponseBodyDataCaseResult(DaraModel):
    def __init__(
        self,
        case_domain: main_models.RunSearchCaseFullTextResponseBodyDataCaseResultCaseDomain = None,
        mode: str = None,
        similarity: str = None,
    ):
        self.case_domain = case_domain
        self.mode = mode
        self.similarity = similarity

    def validate(self):
        if self.case_domain:
            self.case_domain.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.case_domain is not None:
            result['caseDomain'] = self.case_domain.to_map()

        if self.mode is not None:
            result['mode'] = self.mode

        if self.similarity is not None:
            result['similarity'] = self.similarity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('caseDomain') is not None:
            temp_model = main_models.RunSearchCaseFullTextResponseBodyDataCaseResultCaseDomain()
            self.case_domain = temp_model.from_map(m.get('caseDomain'))

        if m.get('mode') is not None:
            self.mode = m.get('mode')

        if m.get('similarity') is not None:
            self.similarity = m.get('similarity')

        return self

class RunSearchCaseFullTextResponseBodyDataCaseResultCaseDomain(DaraModel):
    def __init__(
        self,
        abstract_obj: str = None,
        applied_laws: str = None,
        basic_case: str = None,
        case_basic: str = None,
        case_cause: str = None,
        case_feature: str = None,
        case_id: str = None,
        case_no: str = None,
        case_summary: str = None,
        case_title: str = None,
        case_type: str = None,
        close_case_cause: str = None,
        court_find_out: str = None,
        court_think: str = None,
        data_from: str = None,
        dispute_focus: str = None,
        dispute_focus_tag: List[str] = None,
        disputedpoints: str = None,
        document_type: str = None,
        judg_reason: str = None,
        keyfacts: str = None,
        legal_basis: str = None,
        litigants: str = None,
        litigation_participant: str = None,
        open_case_cause: str = None,
        pre_trial_process: str = None,
        refer_level: str = None,
        referee_gist: str = None,
        source_content: str = None,
        trial_court: main_models.RunSearchCaseFullTextResponseBodyDataCaseResultCaseDomainTrialCourt = None,
        trial_date: str = None,
        trial_level: str = None,
        trial_process: str = None,
        trial_program: str = None,
        verdict: str = None,
    ):
        self.abstract_obj = abstract_obj
        self.applied_laws = applied_laws
        self.basic_case = basic_case
        self.case_basic = case_basic
        self.case_cause = case_cause
        self.case_feature = case_feature
        self.case_id = case_id
        self.case_no = case_no
        self.case_summary = case_summary
        self.case_title = case_title
        self.case_type = case_type
        self.close_case_cause = close_case_cause
        self.court_find_out = court_find_out
        self.court_think = court_think
        self.data_from = data_from
        self.dispute_focus = dispute_focus
        self.dispute_focus_tag = dispute_focus_tag
        self.disputedpoints = disputedpoints
        self.document_type = document_type
        self.judg_reason = judg_reason
        self.keyfacts = keyfacts
        self.legal_basis = legal_basis
        self.litigants = litigants
        self.litigation_participant = litigation_participant
        self.open_case_cause = open_case_cause
        self.pre_trial_process = pre_trial_process
        self.refer_level = refer_level
        self.referee_gist = referee_gist
        self.source_content = source_content
        self.trial_court = trial_court
        self.trial_date = trial_date
        self.trial_level = trial_level
        self.trial_process = trial_process
        self.trial_program = trial_program
        self.verdict = verdict

    def validate(self):
        if self.trial_court:
            self.trial_court.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abstract_obj is not None:
            result['abstractObj'] = self.abstract_obj

        if self.applied_laws is not None:
            result['appliedLaws'] = self.applied_laws

        if self.basic_case is not None:
            result['basicCase'] = self.basic_case

        if self.case_basic is not None:
            result['caseBasic'] = self.case_basic

        if self.case_cause is not None:
            result['caseCause'] = self.case_cause

        if self.case_feature is not None:
            result['caseFeature'] = self.case_feature

        if self.case_id is not None:
            result['caseId'] = self.case_id

        if self.case_no is not None:
            result['caseNo'] = self.case_no

        if self.case_summary is not None:
            result['caseSummary'] = self.case_summary

        if self.case_title is not None:
            result['caseTitle'] = self.case_title

        if self.case_type is not None:
            result['caseType'] = self.case_type

        if self.close_case_cause is not None:
            result['closeCaseCause'] = self.close_case_cause

        if self.court_find_out is not None:
            result['courtFindOut'] = self.court_find_out

        if self.court_think is not None:
            result['courtThink'] = self.court_think

        if self.data_from is not None:
            result['dataFrom'] = self.data_from

        if self.dispute_focus is not None:
            result['disputeFocus'] = self.dispute_focus

        if self.dispute_focus_tag is not None:
            result['disputeFocusTag'] = self.dispute_focus_tag

        if self.disputedpoints is not None:
            result['disputedpoints'] = self.disputedpoints

        if self.document_type is not None:
            result['documentType'] = self.document_type

        if self.judg_reason is not None:
            result['judgReason'] = self.judg_reason

        if self.keyfacts is not None:
            result['keyfacts'] = self.keyfacts

        if self.legal_basis is not None:
            result['legalBasis'] = self.legal_basis

        if self.litigants is not None:
            result['litigants'] = self.litigants

        if self.litigation_participant is not None:
            result['litigationParticipant'] = self.litigation_participant

        if self.open_case_cause is not None:
            result['openCaseCause'] = self.open_case_cause

        if self.pre_trial_process is not None:
            result['preTrialProcess'] = self.pre_trial_process

        if self.refer_level is not None:
            result['referLevel'] = self.refer_level

        if self.referee_gist is not None:
            result['refereeGist'] = self.referee_gist

        if self.source_content is not None:
            result['sourceContent'] = self.source_content

        if self.trial_court is not None:
            result['trialCourt'] = self.trial_court.to_map()

        if self.trial_date is not None:
            result['trialDate'] = self.trial_date

        if self.trial_level is not None:
            result['trialLevel'] = self.trial_level

        if self.trial_process is not None:
            result['trialProcess'] = self.trial_process

        if self.trial_program is not None:
            result['trialProgram'] = self.trial_program

        if self.verdict is not None:
            result['verdict'] = self.verdict

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('abstractObj') is not None:
            self.abstract_obj = m.get('abstractObj')

        if m.get('appliedLaws') is not None:
            self.applied_laws = m.get('appliedLaws')

        if m.get('basicCase') is not None:
            self.basic_case = m.get('basicCase')

        if m.get('caseBasic') is not None:
            self.case_basic = m.get('caseBasic')

        if m.get('caseCause') is not None:
            self.case_cause = m.get('caseCause')

        if m.get('caseFeature') is not None:
            self.case_feature = m.get('caseFeature')

        if m.get('caseId') is not None:
            self.case_id = m.get('caseId')

        if m.get('caseNo') is not None:
            self.case_no = m.get('caseNo')

        if m.get('caseSummary') is not None:
            self.case_summary = m.get('caseSummary')

        if m.get('caseTitle') is not None:
            self.case_title = m.get('caseTitle')

        if m.get('caseType') is not None:
            self.case_type = m.get('caseType')

        if m.get('closeCaseCause') is not None:
            self.close_case_cause = m.get('closeCaseCause')

        if m.get('courtFindOut') is not None:
            self.court_find_out = m.get('courtFindOut')

        if m.get('courtThink') is not None:
            self.court_think = m.get('courtThink')

        if m.get('dataFrom') is not None:
            self.data_from = m.get('dataFrom')

        if m.get('disputeFocus') is not None:
            self.dispute_focus = m.get('disputeFocus')

        if m.get('disputeFocusTag') is not None:
            self.dispute_focus_tag = m.get('disputeFocusTag')

        if m.get('disputedpoints') is not None:
            self.disputedpoints = m.get('disputedpoints')

        if m.get('documentType') is not None:
            self.document_type = m.get('documentType')

        if m.get('judgReason') is not None:
            self.judg_reason = m.get('judgReason')

        if m.get('keyfacts') is not None:
            self.keyfacts = m.get('keyfacts')

        if m.get('legalBasis') is not None:
            self.legal_basis = m.get('legalBasis')

        if m.get('litigants') is not None:
            self.litigants = m.get('litigants')

        if m.get('litigationParticipant') is not None:
            self.litigation_participant = m.get('litigationParticipant')

        if m.get('openCaseCause') is not None:
            self.open_case_cause = m.get('openCaseCause')

        if m.get('preTrialProcess') is not None:
            self.pre_trial_process = m.get('preTrialProcess')

        if m.get('referLevel') is not None:
            self.refer_level = m.get('referLevel')

        if m.get('refereeGist') is not None:
            self.referee_gist = m.get('refereeGist')

        if m.get('sourceContent') is not None:
            self.source_content = m.get('sourceContent')

        if m.get('trialCourt') is not None:
            temp_model = main_models.RunSearchCaseFullTextResponseBodyDataCaseResultCaseDomainTrialCourt()
            self.trial_court = temp_model.from_map(m.get('trialCourt'))

        if m.get('trialDate') is not None:
            self.trial_date = m.get('trialDate')

        if m.get('trialLevel') is not None:
            self.trial_level = m.get('trialLevel')

        if m.get('trialProcess') is not None:
            self.trial_process = m.get('trialProcess')

        if m.get('trialProgram') is not None:
            self.trial_program = m.get('trialProgram')

        if m.get('verdict') is not None:
            self.verdict = m.get('verdict')

        return self

class RunSearchCaseFullTextResponseBodyDataCaseResultCaseDomainTrialCourt(DaraModel):
    def __init__(
        self,
        city: str = None,
        common_level: str = None,
        country: str = None,
        county: str = None,
        district: str = None,
        name: str = None,
        province: str = None,
        special_level: str = None,
    ):
        self.city = city
        self.common_level = common_level
        self.country = country
        self.county = county
        self.district = district
        self.name = name
        self.province = province
        self.special_level = special_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.city is not None:
            result['city'] = self.city

        if self.common_level is not None:
            result['commonLevel'] = self.common_level

        if self.country is not None:
            result['country'] = self.country

        if self.county is not None:
            result['county'] = self.county

        if self.district is not None:
            result['district'] = self.district

        if self.name is not None:
            result['name'] = self.name

        if self.province is not None:
            result['province'] = self.province

        if self.special_level is not None:
            result['specialLevel'] = self.special_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('city') is not None:
            self.city = m.get('city')

        if m.get('commonLevel') is not None:
            self.common_level = m.get('commonLevel')

        if m.get('country') is not None:
            self.country = m.get('country')

        if m.get('county') is not None:
            self.county = m.get('county')

        if m.get('district') is not None:
            self.district = m.get('district')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('province') is not None:
            self.province = m.get('province')

        if m.get('specialLevel') is not None:
            self.special_level = m.get('specialLevel')

        return self

