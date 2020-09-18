# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List


class ListTemplatesRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, name=None, tag=None, lang=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.name = name                # type: str
        self.tag = tag                  # type: str
        self.lang = lang                # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['Name'] = self.name
        result['Tag'] = self.tag
        result['Lang'] = self.lang
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.name = map.get('Name')
        self.tag = map.get('Tag')
        self.lang = map.get('Lang')
        return self


class ListTemplatesResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, templates=None):
        self.request_id = request_id    # type: str
        self.total_count = total_count  # type: int
        self.templates = templates      # type: List[ListTemplatesResponseTemplates]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.templates, 'templates')
        if self.templates:
            for k in self.templates:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['Templates'] = []
        if self.templates is not None:
            for k in self.templates:
                result['Templates'].append(k.to_map() if k else None)
        else:
            result['Templates'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.templates = []
        if map.get('Templates') is not None:
            for k in map.get('Templates'):
                temp_model = ListTemplatesResponseTemplates()
                self.templates.append(temp_model.from_map(k))
        else:
            self.templates = None
        return self


class ListTemplatesResponseTemplates(TeaModel):
    def __init__(self, template_id=None, template_name=None, template_description=None, template_tag=None,
                 create_time=None, update_time=None, template_connector=None, template_summary=None, template_summary_en=None,
                 template_locale=None, template_version=None, template_creator=None, template_overview=None):
        self.template_id = template_id  # type: str
        self.template_name = template_name  # type: str
        self.template_description = template_description  # type: str
        self.template_tag = template_tag  # type: str
        self.create_time = create_time  # type: str
        self.update_time = update_time  # type: str
        self.template_connector = template_connector  # type: str
        self.template_summary = template_summary  # type: str
        self.template_summary_en = template_summary_en  # type: str
        self.template_locale = template_locale  # type: str
        self.template_version = template_version  # type: int
        self.template_creator = template_creator  # type: str
        self.template_overview = template_overview  # type: str

    def validate(self):
        self.validate_required(self.template_id, 'template_id')
        self.validate_required(self.template_name, 'template_name')
        self.validate_required(self.template_description, 'template_description')
        self.validate_required(self.template_tag, 'template_tag')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.template_connector, 'template_connector')
        self.validate_required(self.template_summary, 'template_summary')
        self.validate_required(self.template_summary_en, 'template_summary_en')
        self.validate_required(self.template_locale, 'template_locale')
        self.validate_required(self.template_version, 'template_version')
        self.validate_required(self.template_creator, 'template_creator')
        self.validate_required(self.template_overview, 'template_overview')

    def to_map(self):
        result = {}
        result['TemplateId'] = self.template_id
        result['TemplateName'] = self.template_name
        result['TemplateDescription'] = self.template_description
        result['TemplateTag'] = self.template_tag
        result['CreateTime'] = self.create_time
        result['UpdateTime'] = self.update_time
        result['TemplateConnector'] = self.template_connector
        result['TemplateSummary'] = self.template_summary
        result['TemplateSummaryEn'] = self.template_summary_en
        result['TemplateLocale'] = self.template_locale
        result['TemplateVersion'] = self.template_version
        result['TemplateCreator'] = self.template_creator
        result['TemplateOverview'] = self.template_overview
        return result

    def from_map(self, map={}):
        self.template_id = map.get('TemplateId')
        self.template_name = map.get('TemplateName')
        self.template_description = map.get('TemplateDescription')
        self.template_tag = map.get('TemplateTag')
        self.create_time = map.get('CreateTime')
        self.update_time = map.get('UpdateTime')
        self.template_connector = map.get('TemplateConnector')
        self.template_summary = map.get('TemplateSummary')
        self.template_summary_en = map.get('TemplateSummaryEn')
        self.template_locale = map.get('TemplateLocale')
        self.template_version = map.get('TemplateVersion')
        self.template_creator = map.get('TemplateCreator')
        self.template_overview = map.get('TemplateOverview')
        return self


class GetTemplateRequest(TeaModel):
    def __init__(self, template_id=None):
        self.template_id = template_id  # type: str

    def validate(self):
        self.validate_required(self.template_id, 'template_id')

    def to_map(self):
        result = {}
        result['TemplateId'] = self.template_id
        return result

    def from_map(self, map={}):
        self.template_id = map.get('TemplateId')
        return self


class GetTemplateResponse(TeaModel):
    def __init__(self, request_id=None, region_id=None, template_id=None, template_name=None,
                 template_description=None, template_tag=None, definition=None, create_time=None, update_time=None,
                 template_connector=None, template_summary=None, template_summary_en=None, template_locale=None,
                 template_version=None, template_overview=None, template_creator=None):
        self.request_id = request_id    # type: str
        self.region_id = region_id      # type: str
        self.template_id = template_id  # type: str
        self.template_name = template_name  # type: str
        self.template_description = template_description  # type: str
        self.template_tag = template_tag  # type: str
        self.definition = definition    # type: str
        self.create_time = create_time  # type: str
        self.update_time = update_time  # type: str
        self.template_connector = template_connector  # type: str
        self.template_summary = template_summary  # type: str
        self.template_summary_en = template_summary_en  # type: str
        self.template_locale = template_locale  # type: str
        self.template_version = template_version  # type: int
        self.template_overview = template_overview  # type: str
        self.template_creator = template_creator  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.template_id, 'template_id')
        self.validate_required(self.template_name, 'template_name')
        self.validate_required(self.template_description, 'template_description')
        self.validate_required(self.template_tag, 'template_tag')
        self.validate_required(self.definition, 'definition')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.template_connector, 'template_connector')
        self.validate_required(self.template_summary, 'template_summary')
        self.validate_required(self.template_summary_en, 'template_summary_en')
        self.validate_required(self.template_locale, 'template_locale')
        self.validate_required(self.template_version, 'template_version')
        self.validate_required(self.template_overview, 'template_overview')
        self.validate_required(self.template_creator, 'template_creator')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['RegionId'] = self.region_id
        result['TemplateId'] = self.template_id
        result['TemplateName'] = self.template_name
        result['TemplateDescription'] = self.template_description
        result['TemplateTag'] = self.template_tag
        result['Definition'] = self.definition
        result['CreateTime'] = self.create_time
        result['UpdateTime'] = self.update_time
        result['TemplateConnector'] = self.template_connector
        result['TemplateSummary'] = self.template_summary
        result['TemplateSummaryEn'] = self.template_summary_en
        result['TemplateLocale'] = self.template_locale
        result['TemplateVersion'] = self.template_version
        result['TemplateOverview'] = self.template_overview
        result['TemplateCreator'] = self.template_creator
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.region_id = map.get('RegionId')
        self.template_id = map.get('TemplateId')
        self.template_name = map.get('TemplateName')
        self.template_description = map.get('TemplateDescription')
        self.template_tag = map.get('TemplateTag')
        self.definition = map.get('Definition')
        self.create_time = map.get('CreateTime')
        self.update_time = map.get('UpdateTime')
        self.template_connector = map.get('TemplateConnector')
        self.template_summary = map.get('TemplateSummary')
        self.template_summary_en = map.get('TemplateSummaryEn')
        self.template_locale = map.get('TemplateLocale')
        self.template_version = map.get('TemplateVersion')
        self.template_overview = map.get('TemplateOverview')
        self.template_creator = map.get('TemplateCreator')
        return self


class GroupInvokeFlowRequest(TeaModel):
    def __init__(self, flow_id=None, group_key=None, data=None, client_token=None, total_count=None):
        self.flow_id = flow_id          # type: str
        self.group_key = group_key      # type: str
        self.data = data                # type: str
        self.client_token = client_token  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        self.validate_required(self.flow_id, 'flow_id')
        self.validate_required(self.group_key, 'group_key')
        self.validate_required(self.data, 'data')
        self.validate_required(self.client_token, 'client_token')
        self.validate_required(self.total_count, 'total_count')

    def to_map(self):
        result = {}
        result['FlowId'] = self.flow_id
        result['GroupKey'] = self.group_key
        result['Data'] = self.data
        result['ClientToken'] = self.client_token
        result['TotalCount'] = self.total_count
        return result

    def from_map(self, map={}):
        self.flow_id = map.get('FlowId')
        self.group_key = map.get('GroupKey')
        self.data = map.get('Data')
        self.client_token = map.get('ClientToken')
        self.total_count = map.get('TotalCount')
        return self


class GroupInvokeFlowResponse(TeaModel):
    def __init__(self, request_id=None, group_invocation_id=None, success=None, current_count=None, status=None):
        self.request_id = request_id    # type: str
        self.group_invocation_id = group_invocation_id  # type: str
        self.success = success          # type: bool
        self.current_count = current_count  # type: int
        self.status = status            # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.group_invocation_id, 'group_invocation_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.current_count, 'current_count')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['GroupInvocationId'] = self.group_invocation_id
        result['Success'] = self.success
        result['CurrentCount'] = self.current_count
        result['Status'] = self.status
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.group_invocation_id = map.get('GroupInvocationId')
        self.success = map.get('Success')
        self.current_count = map.get('CurrentCount')
        self.status = map.get('Status')
        return self


class ListTagResourcesRequest(TeaModel):
    def __init__(self, resource_type=None, resource_id=None, tag=None, next_token=None, max_results=None):
        self.resource_type = resource_type  # type: str
        self.resource_id = resource_id  # type: List[str]
        self.tag = tag                  # type: List[ListTagResourcesRequestTag]
        self.next_token = next_token    # type: str
        self.max_results = max_results  # type: int

    def validate(self):
        self.validate_required(self.resource_type, 'resource_type')
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['ResourceType'] = self.resource_type
        result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        else:
            result['Tag'] = None
        result['NextToken'] = self.next_token
        result['MaxResults'] = self.max_results
        return result

    def from_map(self, map={}):
        self.resource_type = map.get('ResourceType')
        self.resource_id = map.get('ResourceId')
        self.tag = []
        if map.get('Tag') is not None:
            for k in map.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        else:
            self.tag = None
        self.next_token = map.get('NextToken')
        self.max_results = map.get('MaxResults')
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key                  # type: str
        self.value = value              # type: str

    def validate(self):
        self.validate_required(self.key, 'key')
        self.validate_required(self.value, 'value')

    def to_map(self):
        result = {}
        result['Key'] = self.key
        result['Value'] = self.value
        return result

    def from_map(self, map={}):
        self.key = map.get('Key')
        self.value = map.get('Value')
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(self, request_id=None, next_token=None, total_count=None, tag_resources=None):
        self.request_id = request_id    # type: str
        self.next_token = next_token    # type: str
        self.total_count = total_count  # type: int
        self.tag_resources = tag_resources  # type: List[ListTagResourcesResponseTagResources]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.next_token, 'next_token')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.tag_resources, 'tag_resources')
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['NextToken'] = self.next_token
        result['TotalCount'] = self.total_count
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        else:
            result['TagResources'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.next_token = map.get('NextToken')
        self.total_count = map.get('TotalCount')
        self.tag_resources = []
        if map.get('TagResources') is not None:
            for k in map.get('TagResources'):
                temp_model = ListTagResourcesResponseTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        else:
            self.tag_resources = None
        return self


class ListTagResourcesResponseTagResources(TeaModel):
    def __init__(self, tag_key=None, tag_value=None, resource_id=None, resource_type=None):
        self.tag_key = tag_key          # type: str
        self.tag_value = tag_value      # type: str
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: str

    def validate(self):
        self.validate_required(self.tag_key, 'tag_key')
        self.validate_required(self.tag_value, 'tag_value')
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.resource_type, 'resource_type')

    def to_map(self):
        result = {}
        result['TagKey'] = self.tag_key
        result['TagValue'] = self.tag_value
        result['ResourceId'] = self.resource_id
        result['ResourceType'] = self.resource_type
        return result

    def from_map(self, map={}):
        self.tag_key = map.get('TagKey')
        self.tag_value = map.get('TagValue')
        self.resource_id = map.get('ResourceId')
        self.resource_type = map.get('ResourceType')
        return self


class TagResourcesRequest(TeaModel):
    def __init__(self, resource_type=None, resource_id=None, tag=None):
        self.resource_type = resource_type  # type: str
        self.resource_id = resource_id  # type: List[str]
        self.tag = tag                  # type: List[TagResourcesRequestTag]

    def validate(self):
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.tag, 'tag')
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['ResourceType'] = self.resource_type
        result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        else:
            result['Tag'] = None
        return result

    def from_map(self, map={}):
        self.resource_type = map.get('ResourceType')
        self.resource_id = map.get('ResourceId')
        self.tag = []
        if map.get('Tag') is not None:
            for k in map.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        else:
            self.tag = None
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key                  # type: str
        self.value = value              # type: str

    def validate(self):
        self.validate_required(self.key, 'key')
        self.validate_required(self.value, 'value')

    def to_map(self):
        result = {}
        result['Key'] = self.key
        result['Value'] = self.value
        return result

    def from_map(self, map={}):
        self.key = map.get('Key')
        self.value = map.get('Value')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(self, resource_type=None, resource_id=None, tag_key=None, all=None):
        self.resource_type = resource_type  # type: str
        self.resource_id = resource_id  # type: List[str]
        self.tag_key = tag_key          # type: List[str]
        self.all = all                  # type: bool

    def validate(self):
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        result = {}
        result['ResourceType'] = self.resource_type
        result['ResourceId'] = self.resource_id
        result['TagKey'] = self.tag_key
        result['All'] = self.all
        return result

    def from_map(self, map={}):
        self.resource_type = map.get('ResourceType')
        self.resource_id = map.get('ResourceId')
        self.tag_key = map.get('TagKey')
        self.all = map.get('All')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        return self


class GetVersionRequest(TeaModel):
    def __init__(self, flow_id=None, version_id=None):
        self.flow_id = flow_id          # type: str
        self.version_id = version_id    # type: int

    def validate(self):
        self.validate_required(self.flow_id, 'flow_id')
        self.validate_required(self.version_id, 'version_id')

    def to_map(self):
        result = {}
        result['FlowId'] = self.flow_id
        result['VersionId'] = self.version_id
        return result

    def from_map(self, map={}):
        self.flow_id = map.get('FlowId')
        self.version_id = map.get('VersionId')
        return self


class GetVersionResponse(TeaModel):
    def __init__(self, request_id=None, flow_id=None, region_id=None, version_name=None, version_description=None,
                 definition=None, create_time=None, update_time=None, version_id=None, version_status=None):
        self.request_id = request_id    # type: str
        self.flow_id = flow_id          # type: str
        self.region_id = region_id      # type: str
        self.version_name = version_name  # type: str
        self.version_description = version_description  # type: str
        self.definition = definition    # type: str
        self.create_time = create_time  # type: str
        self.update_time = update_time  # type: str
        self.version_id = version_id    # type: int
        self.version_status = version_status  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.flow_id, 'flow_id')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.version_name, 'version_name')
        self.validate_required(self.version_description, 'version_description')
        self.validate_required(self.definition, 'definition')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.version_id, 'version_id')
        self.validate_required(self.version_status, 'version_status')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['FlowId'] = self.flow_id
        result['RegionId'] = self.region_id
        result['VersionName'] = self.version_name
        result['VersionDescription'] = self.version_description
        result['Definition'] = self.definition
        result['CreateTime'] = self.create_time
        result['UpdateTime'] = self.update_time
        result['VersionId'] = self.version_id
        result['VersionStatus'] = self.version_status
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.flow_id = map.get('FlowId')
        self.region_id = map.get('RegionId')
        self.version_name = map.get('VersionName')
        self.version_description = map.get('VersionDescription')
        self.definition = map.get('Definition')
        self.create_time = map.get('CreateTime')
        self.update_time = map.get('UpdateTime')
        self.version_id = map.get('VersionId')
        self.version_status = map.get('VersionStatus')
        return self


class ListVersionsRequest(TeaModel):
    def __init__(self, flow_id=None, page_number=None, page_size=None):
        self.flow_id = flow_id          # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        self.validate_required(self.flow_id, 'flow_id')

    def to_map(self):
        result = {}
        result['FlowId'] = self.flow_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.flow_id = map.get('FlowId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        return self


class ListVersionsResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, versions=None):
        self.request_id = request_id    # type: str
        self.total_count = total_count  # type: int
        self.versions = versions        # type: List[ListVersionsResponseVersions]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.versions, 'versions')
        if self.versions:
            for k in self.versions:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['Versions'] = []
        if self.versions is not None:
            for k in self.versions:
                result['Versions'].append(k.to_map() if k else None)
        else:
            result['Versions'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.versions = []
        if map.get('Versions') is not None:
            for k in map.get('Versions'):
                temp_model = ListVersionsResponseVersions()
                self.versions.append(temp_model.from_map(k))
        else:
            self.versions = None
        return self


class ListVersionsResponseVersions(TeaModel):
    def __init__(self, version_id=None, flow_id=None, version_name=None, version_status=None, create_time=None,
                 update_time=None):
        self.version_id = version_id    # type: str
        self.flow_id = flow_id          # type: str
        self.version_name = version_name  # type: int
        self.version_status = version_status  # type: int
        self.create_time = create_time  # type: str
        self.update_time = update_time  # type: str

    def validate(self):
        self.validate_required(self.version_id, 'version_id')
        self.validate_required(self.flow_id, 'flow_id')
        self.validate_required(self.version_name, 'version_name')
        self.validate_required(self.version_status, 'version_status')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.update_time, 'update_time')

    def to_map(self):
        result = {}
        result['VersionId'] = self.version_id
        result['FlowId'] = self.flow_id
        result['VersionName'] = self.version_name
        result['VersionStatus'] = self.version_status
        result['CreateTime'] = self.create_time
        result['UpdateTime'] = self.update_time
        return result

    def from_map(self, map={}):
        self.version_id = map.get('VersionId')
        self.flow_id = map.get('FlowId')
        self.version_name = map.get('VersionName')
        self.version_status = map.get('VersionStatus')
        self.create_time = map.get('CreateTime')
        self.update_time = map.get('UpdateTime')
        return self


class UpdateFlowRequest(TeaModel):
    def __init__(self, flow_id=None, flow_name=None, flow_description=None, definition=None):
        self.flow_id = flow_id          # type: str
        self.flow_name = flow_name      # type: str
        self.flow_description = flow_description  # type: str
        self.definition = definition    # type: str

    def validate(self):
        self.validate_required(self.flow_id, 'flow_id')

    def to_map(self):
        result = {}
        result['FlowId'] = self.flow_id
        result['FlowName'] = self.flow_name
        result['FlowDescription'] = self.flow_description
        result['Definition'] = self.definition
        return result

    def from_map(self, map={}):
        self.flow_id = map.get('FlowId')
        self.flow_name = map.get('FlowName')
        self.flow_description = map.get('FlowDescription')
        self.definition = map.get('Definition')
        return self


class UpdateFlowResponse(TeaModel):
    def __init__(self, request_id=None, success=None, current_version_id=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.current_version_id = current_version_id  # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.current_version_id, 'current_version_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['CurrentVersionId'] = self.current_version_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.current_version_id = map.get('CurrentVersionId')
        return self


class CloneFlowRequest(TeaModel):
    def __init__(self, flow_id=None, version_id=None):
        self.flow_id = flow_id          # type: str
        self.version_id = version_id    # type: str

    def validate(self):
        self.validate_required(self.flow_id, 'flow_id')

    def to_map(self):
        result = {}
        result['FlowId'] = self.flow_id
        result['VersionId'] = self.version_id
        return result

    def from_map(self, map={}):
        self.flow_id = map.get('FlowId')
        self.version_id = map.get('VersionId')
        return self


class CloneFlowResponse(TeaModel):
    def __init__(self, request_id=None, flow_id=None):
        self.request_id = request_id    # type: str
        self.flow_id = flow_id          # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.flow_id, 'flow_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['FlowId'] = self.flow_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.flow_id = map.get('FlowId')
        return self


class GetFlowRequest(TeaModel):
    def __init__(self, flow_id=None):
        self.flow_id = flow_id          # type: str

    def validate(self):
        self.validate_required(self.flow_id, 'flow_id')

    def to_map(self):
        result = {}
        result['FlowId'] = self.flow_id
        return result

    def from_map(self, map={}):
        self.flow_id = map.get('FlowId')
        return self


class GetFlowResponse(TeaModel):
    def __init__(self, request_id=None, flow_id=None, region_id=None, flow_name=None, flow_description=None,
                 create_time=None, update_time=None, current_version_id=None, flow_status=None, definition=None,
                 template_id=None, flow_source=None, flow_edit_mode=None):
        self.request_id = request_id    # type: str
        self.flow_id = flow_id          # type: str
        self.region_id = region_id      # type: str
        self.flow_name = flow_name      # type: str
        self.flow_description = flow_description  # type: str
        self.create_time = create_time  # type: str
        self.update_time = update_time  # type: str
        self.current_version_id = current_version_id  # type: int
        self.flow_status = flow_status  # type: str
        self.definition = definition    # type: str
        self.template_id = template_id  # type: str
        self.flow_source = flow_source  # type: str
        self.flow_edit_mode = flow_edit_mode  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.flow_id, 'flow_id')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.flow_name, 'flow_name')
        self.validate_required(self.flow_description, 'flow_description')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.current_version_id, 'current_version_id')
        self.validate_required(self.flow_status, 'flow_status')
        self.validate_required(self.definition, 'definition')
        self.validate_required(self.template_id, 'template_id')
        self.validate_required(self.flow_source, 'flow_source')
        self.validate_required(self.flow_edit_mode, 'flow_edit_mode')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['FlowId'] = self.flow_id
        result['RegionId'] = self.region_id
        result['FlowName'] = self.flow_name
        result['FlowDescription'] = self.flow_description
        result['CreateTime'] = self.create_time
        result['UpdateTime'] = self.update_time
        result['CurrentVersionId'] = self.current_version_id
        result['FlowStatus'] = self.flow_status
        result['Definition'] = self.definition
        result['TemplateId'] = self.template_id
        result['FlowSource'] = self.flow_source
        result['FlowEditMode'] = self.flow_edit_mode
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.flow_id = map.get('FlowId')
        self.region_id = map.get('RegionId')
        self.flow_name = map.get('FlowName')
        self.flow_description = map.get('FlowDescription')
        self.create_time = map.get('CreateTime')
        self.update_time = map.get('UpdateTime')
        self.current_version_id = map.get('CurrentVersionId')
        self.flow_status = map.get('FlowStatus')
        self.definition = map.get('Definition')
        self.template_id = map.get('TemplateId')
        self.flow_source = map.get('FlowSource')
        self.flow_edit_mode = map.get('FlowEditMode')
        return self


class ListFlowsRequest(TeaModel):
    def __init__(self, page_size=None, page_number=None, flow_name=None, filter=None):
        self.page_size = page_size      # type: int
        self.page_number = page_number  # type: int
        self.flow_name = flow_name      # type: str
        self.filter = filter            # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['PageSize'] = self.page_size
        result['PageNumber'] = self.page_number
        result['FlowName'] = self.flow_name
        result['Filter'] = self.filter
        return result

    def from_map(self, map={}):
        self.page_size = map.get('PageSize')
        self.page_number = map.get('PageNumber')
        self.flow_name = map.get('FlowName')
        self.filter = map.get('Filter')
        return self


class ListFlowsResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, flows=None):
        self.request_id = request_id    # type: str
        self.total_count = total_count  # type: int
        self.flows = flows              # type: List[ListFlowsResponseFlows]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.flows, 'flows')
        if self.flows:
            for k in self.flows:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['Flows'] = []
        if self.flows is not None:
            for k in self.flows:
                result['Flows'].append(k.to_map() if k else None)
        else:
            result['Flows'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.flows = []
        if map.get('Flows') is not None:
            for k in map.get('Flows'):
                temp_model = ListFlowsResponseFlows()
                self.flows.append(temp_model.from_map(k))
        else:
            self.flows = None
        return self


class ListFlowsResponseFlows(TeaModel):
    def __init__(self, flow_id=None, region_id=None, flow_name=None, flow_description=None, version_id=None,
                 create_time=None, update_time=None, flow_status=None, template_id=None, flow_source=None, flow_edit_mode=None):
        self.flow_id = flow_id          # type: str
        self.region_id = region_id      # type: str
        self.flow_name = flow_name      # type: str
        self.flow_description = flow_description  # type: str
        self.version_id = version_id    # type: int
        self.create_time = create_time  # type: str
        self.update_time = update_time  # type: str
        self.flow_status = flow_status  # type: str
        self.template_id = template_id  # type: str
        self.flow_source = flow_source  # type: str
        self.flow_edit_mode = flow_edit_mode  # type: str

    def validate(self):
        self.validate_required(self.flow_id, 'flow_id')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.flow_name, 'flow_name')
        self.validate_required(self.flow_description, 'flow_description')
        self.validate_required(self.version_id, 'version_id')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.flow_status, 'flow_status')
        self.validate_required(self.template_id, 'template_id')
        self.validate_required(self.flow_source, 'flow_source')
        self.validate_required(self.flow_edit_mode, 'flow_edit_mode')

    def to_map(self):
        result = {}
        result['FlowId'] = self.flow_id
        result['RegionId'] = self.region_id
        result['FlowName'] = self.flow_name
        result['FlowDescription'] = self.flow_description
        result['VersionId'] = self.version_id
        result['CreateTime'] = self.create_time
        result['UpdateTime'] = self.update_time
        result['FlowStatus'] = self.flow_status
        result['TemplateId'] = self.template_id
        result['FlowSource'] = self.flow_source
        result['FlowEditMode'] = self.flow_edit_mode
        return result

    def from_map(self, map={}):
        self.flow_id = map.get('FlowId')
        self.region_id = map.get('RegionId')
        self.flow_name = map.get('FlowName')
        self.flow_description = map.get('FlowDescription')
        self.version_id = map.get('VersionId')
        self.create_time = map.get('CreateTime')
        self.update_time = map.get('UpdateTime')
        self.flow_status = map.get('FlowStatus')
        self.template_id = map.get('TemplateId')
        self.flow_source = map.get('FlowSource')
        self.flow_edit_mode = map.get('FlowEditMode')
        return self


class DeleteFlowRequest(TeaModel):
    def __init__(self, flow_id=None):
        self.flow_id = flow_id          # type: str

    def validate(self):
        self.validate_required(self.flow_id, 'flow_id')

    def to_map(self):
        result = {}
        result['FlowId'] = self.flow_id
        return result

    def from_map(self, map={}):
        self.flow_id = map.get('FlowId')
        return self


class DeleteFlowResponse(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        return self


class DisableFlowRequest(TeaModel):
    def __init__(self, flow_id=None):
        self.flow_id = flow_id          # type: str

    def validate(self):
        self.validate_required(self.flow_id, 'flow_id')

    def to_map(self):
        result = {}
        result['FlowId'] = self.flow_id
        return result

    def from_map(self, map={}):
        self.flow_id = map.get('FlowId')
        return self


class DisableFlowResponse(TeaModel):
    def __init__(self, request_id=None, success=None, flow_status=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.flow_status = flow_status  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.flow_status, 'flow_status')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['FlowStatus'] = self.flow_status
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.flow_status = map.get('FlowStatus')
        return self


class EnableFlowRequest(TeaModel):
    def __init__(self, flow_id=None):
        self.flow_id = flow_id          # type: str

    def validate(self):
        self.validate_required(self.flow_id, 'flow_id')

    def to_map(self):
        result = {}
        result['FlowId'] = self.flow_id
        return result

    def from_map(self, map={}):
        self.flow_id = map.get('FlowId')
        return self


class EnableFlowResponse(TeaModel):
    def __init__(self, request_id=None, success=None, flow_status=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.flow_status = flow_status  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.flow_status, 'flow_status')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['FlowStatus'] = self.flow_status
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.flow_status = map.get('FlowStatus')
        return self


class CreateFlowRequest(TeaModel):
    def __init__(self, flow_name=None, flow_description=None, definition=None, template_id=None, flow_source=None):
        self.flow_name = flow_name      # type: str
        self.flow_description = flow_description  # type: str
        self.definition = definition    # type: str
        self.template_id = template_id  # type: str
        self.flow_source = flow_source  # type: str

    def validate(self):
        self.validate_required(self.flow_name, 'flow_name')

    def to_map(self):
        result = {}
        result['FlowName'] = self.flow_name
        result['FlowDescription'] = self.flow_description
        result['Definition'] = self.definition
        result['TemplateId'] = self.template_id
        result['FlowSource'] = self.flow_source
        return result

    def from_map(self, map={}):
        self.flow_name = map.get('FlowName')
        self.flow_description = map.get('FlowDescription')
        self.definition = map.get('Definition')
        self.template_id = map.get('TemplateId')
        self.flow_source = map.get('FlowSource')
        return self


class CreateFlowResponse(TeaModel):
    def __init__(self, request_id=None, flow_id=None):
        self.request_id = request_id    # type: str
        self.flow_id = flow_id          # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.flow_id, 'flow_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['FlowId'] = self.flow_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.flow_id = map.get('FlowId')
        return self


class InvokeFlowRequest(TeaModel):
    def __init__(self, flow_id=None, parameters=None, data=None, client_token=None):
        self.flow_id = flow_id          # type: str
        self.parameters = parameters    # type: str
        self.data = data                # type: str
        self.client_token = client_token  # type: str

    def validate(self):
        self.validate_required(self.flow_id, 'flow_id')

    def to_map(self):
        result = {}
        result['FlowId'] = self.flow_id
        result['Parameters'] = self.parameters
        result['Data'] = self.data
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.flow_id = map.get('FlowId')
        self.parameters = map.get('Parameters')
        self.data = map.get('Data')
        self.client_token = map.get('ClientToken')
        return self


class InvokeFlowResponse(TeaModel):
    def __init__(self, request_id=None, invocation_id=None, success=None):
        self.request_id = request_id    # type: str
        self.invocation_id = invocation_id  # type: str
        self.success = success          # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.invocation_id, 'invocation_id')
        self.validate_required(self.success, 'success')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['InvocationId'] = self.invocation_id
        result['Success'] = self.success
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.invocation_id = map.get('InvocationId')
        self.success = map.get('Success')
        return self
