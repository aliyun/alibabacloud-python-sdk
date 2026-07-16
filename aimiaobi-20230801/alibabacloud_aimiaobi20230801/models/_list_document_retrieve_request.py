# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDocumentRetrieveRequest(DaraModel):
    def __init__(
        self,
        content_type: str = None,
        element_scope: str = None,
        end_date: str = None,
        max_results: int = None,
        next_token: str = None,
        office: str = None,
        query: str = None,
        region: str = None,
        source: str = None,
        start_date: str = None,
        sub_content_type: str = None,
        subject_classify: str = None,
        word_size: str = None,
        workspace_id: str = None,
    ):
        # Document type. Valid values: 0 (default): All types. 1: Government documents. 2: Important articles. 5: Policy interpretation. 6: Legal provisions. 7: Regulations and rules. 8: General Secretary.
        self.content_type = content_type
        # Search scope. Valid values: 1: Title only. 0: Full text (title and content). Default is 0.
        self.element_scope = element_scope
        # End date of issuance in yyyy-MM-dd format.
        self.end_date = end_date
        # Maximum number of results to return.
        self.max_results = max_results
        # Token for the next page of results.
        self.next_token = next_token
        # Issuing agency.
        self.office = office
        # Search condition.
        self.query = query
        # Region. Enter a province or city, such as Jilin Province or Beijing Municipality.
        self.region = region
        # Source. Valid values: 0: Internal (within your organization). 1: External (outside your organization).
        self.source = source
        # Start date of issuance in yyyy-MM-dd format.
        self.start_date = start_date
        # - Secondary classification of document type.
        # 
        #   - When the document type is an official document: -1: Other; 0: Resolution; 1: Decision; 2: Order; 3: Bulletin; 4: Public Notice; 5: Notice; 6: Opinion; 7: Notification; 8: Circular; 9: Report; 10: Request for Instructions; 11: Approval; 12: Motion; 13: Letter
        # 
        #   - 14: Summary
        # 
        #   - When the article type is important articles: 1: important commentary 2: important theory 3: other articles
        # 
        #   - When the document genre is rules and regulations: 3: Administrative regulations 4: Supervisory regulations 5: Local regulations 7: Departmental rules 8: Others 9: Party constitution and regulations
        # 
        #   - When the article genre is a legal provision: 1: Constitution 2: Law 6: Judicial Interpretation
        self.sub_content_type = sub_content_type
        # Supported classifications:
        # 
        # | Level 1 category                                                        | Level 2 category                                                                                                                                                                                                                                  |
        # | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        # | National defense and international cooperation                          | National defense. Foreign affairs. Military affairs. Work related to Hong Kong, Macao, Taiwan, and overseas Chinese.                                                                                                                              |
        # | Comprehensive administration                                            | The 20th National Congress of the Communist Party of China. Government transparency and supervision. Joint administration. Party building. Conferences and proposals. Government document management. Other administrative matters.               |
        # | State Council organizational structure                                  | State Council. General Office of the State Council. State Council agencies.                                                                                                                                                                       |
        # | Administrative and market regulation                                    | Administrative regulation. Credit regulation. Product quality supervision. Work safety supervision. Market regulation.                                                                                                                            |
        # | Economic management                                                     | National economy. Market economy. Economic system reform. State-owned asset supervision.                                                                                                                                                          |
        # | Finance, banking, commerce, and customs                                 | Finance. Banking. Auditing. Commerce. Customs.                                                                                                                                                                                                    |
        # | Personnel and social security                                           | Personnel work. Population and family planning. Work related to women and children. Poverty alleviation. Disaster reduction and relief. Public services. Social welfare and assistance. Preferential treatment and resettlement. Social security. |
        # | Public security and social management                                   | Public security. Safety. Justice. Fire control. Ethnic affairs. Religion.                                                                                                                                                                         |
        # | Science, education, culture, and sports                                 | Culture. Scientific and technological innovation. Education. Intellectual property. Press and publishing. Radio, television, and the Internet. Sports. Tourism.                                                                                   |
        # | Healthcare                                                              | Health. Medical care. Veterinary medicine.                                                                                                                                                                                                        |
        # | Urban-rural development and industrial growth                           | Urban and rural development. Industry. Transportation.                                                                                                                                                                                            |
        # | Natural resources and environmental protection                          | Land and energy resources. Civil engineering. Meteorology. Environmental protection.                                                                                                                                                              |
        # | Agriculture, forestry, water resources, fisheries, and animal husbandry | Agriculture. Forestry. Water resources. Fisheries. Animal husbandry.                                                                                                                                                                              |
        # | Others                                                                  | Others.                                                                                                                                                                                                                                           |
        self.subject_classify = subject_classify
        # Document number.
        self.word_size = word_size
        # Unique identifier of the Model Studio workspace. For more information, see [Get workspaceId](https://help.aliyun.com/document_detail/2782167.html).
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.element_scope is not None:
            result['ElementScope'] = self.element_scope

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.office is not None:
            result['Office'] = self.office

        if self.query is not None:
            result['Query'] = self.query

        if self.region is not None:
            result['Region'] = self.region

        if self.source is not None:
            result['Source'] = self.source

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.sub_content_type is not None:
            result['SubContentType'] = self.sub_content_type

        if self.subject_classify is not None:
            result['SubjectClassify'] = self.subject_classify

        if self.word_size is not None:
            result['WordSize'] = self.word_size

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('ElementScope') is not None:
            self.element_scope = m.get('ElementScope')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Office') is not None:
            self.office = m.get('Office')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('SubContentType') is not None:
            self.sub_content_type = m.get('SubContentType')

        if m.get('SubjectClassify') is not None:
            self.subject_classify = m.get('SubjectClassify')

        if m.get('WordSize') is not None:
            self.word_size = m.get('WordSize')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

