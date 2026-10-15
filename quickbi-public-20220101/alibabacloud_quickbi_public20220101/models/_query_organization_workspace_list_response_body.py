# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class QueryOrganizationWorkspaceListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.QueryOrganizationWorkspaceListResponseBodyResult = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The paginated result of the workspace list. The detailed information of workspaces is stored in the Data response parameter.
        self.result = result
        # Indicates whether the request was successful. Valid values:
        # 
        # - true: The request was successful.
        # - false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.QueryOrganizationWorkspaceListResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryOrganizationWorkspaceListResponseBodyResult(DaraModel):
    def __init__(
        self,
        data: List[main_models.QueryOrganizationWorkspaceListResponseBodyResultData] = None,
        page_num: int = None,
        page_size: int = None,
        total_num: int = None,
        total_pages: int = None,
    ):
        # The list of workspaces.
        self.data = data
        # The page number.
        self.page_num = page_num
        # The number of rows per page specified in the request.
        self.page_size = page_size
        # The total number of rows.
        self.total_num = total_num
        # The total number of pages.
        self.total_pages = total_pages

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QueryOrganizationWorkspaceListResponseBodyResultData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class QueryOrganizationWorkspaceListResponseBodyResultData(DaraModel):
    def __init__(
        self,
        allow_publish_operation: bool = None,
        allow_share_operation: bool = None,
        create_time: str = None,
        create_user: str = None,
        create_user_account_name: str = None,
        modified_time: str = None,
        modify_user: str = None,
        modify_user_account_name: str = None,
        organization_id: str = None,
        owner: str = None,
        owner_account_name: str = None,
        real_owner_account_name: str = None,
        workspace_description: str = None,
        workspace_export_config: main_models.QueryOrganizationWorkspaceListResponseBodyResultDataWorkspaceExportConfig = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        # Indicates whether works can be made public. Valid values:
        # 
        # - true: Public.
        # - false: Not public.
        self.allow_publish_operation = allow_publish_operation
        # Indicates whether works can be shared with authorization. Valid values:
        # 
        # - true: Authorized.
        # - false: Not authorized.
        self.allow_share_operation = allow_share_operation
        # The time when the workspace was created.
        self.create_time = create_time
        # The Quick BI user ID of the creator.
        self.create_user = create_user
        # The Alibaba Cloud account name of the creator.
        self.create_user_account_name = create_user_account_name
        # The time when the workspace was last modified.
        self.modified_time = modified_time
        # The Quick BI user ID of the modifier.
        self.modify_user = modify_user
        # The Alibaba Cloud account name of the modifier.
        self.modify_user_account_name = modify_user_account_name
        # The ID of the organization to which the workspace belongs.
        self.organization_id = organization_id
        # The Quick BI user ID of the workspace owner.
        self.owner = owner
        # The Alibaba Cloud account name of the workspace owner.
        self.owner_account_name = owner_account_name
        # The Quick BI account name of the workspace owner.
        self.real_owner_account_name = real_owner_account_name
        # The description of the workspace.
        self.workspace_description = workspace_description
        # The workspace export configuration.
        self.workspace_export_config = workspace_export_config
        # The workspace ID.
        self.workspace_id = workspace_id
        # The workspace name.
        self.workspace_name = workspace_name

    def validate(self):
        if self.workspace_export_config:
            self.workspace_export_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_publish_operation is not None:
            result['AllowPublishOperation'] = self.allow_publish_operation

        if self.allow_share_operation is not None:
            result['AllowShareOperation'] = self.allow_share_operation

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user is not None:
            result['CreateUser'] = self.create_user

        if self.create_user_account_name is not None:
            result['CreateUserAccountName'] = self.create_user_account_name

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.modify_user is not None:
            result['ModifyUser'] = self.modify_user

        if self.modify_user_account_name is not None:
            result['ModifyUserAccountName'] = self.modify_user_account_name

        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.owner_account_name is not None:
            result['OwnerAccountName'] = self.owner_account_name

        if self.real_owner_account_name is not None:
            result['RealOwnerAccountName'] = self.real_owner_account_name

        if self.workspace_description is not None:
            result['WorkspaceDescription'] = self.workspace_description

        if self.workspace_export_config is not None:
            result['WorkspaceExportConfig'] = self.workspace_export_config.to_map()

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowPublishOperation') is not None:
            self.allow_publish_operation = m.get('AllowPublishOperation')

        if m.get('AllowShareOperation') is not None:
            self.allow_share_operation = m.get('AllowShareOperation')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('CreateUserAccountName') is not None:
            self.create_user_account_name = m.get('CreateUserAccountName')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('ModifyUser') is not None:
            self.modify_user = m.get('ModifyUser')

        if m.get('ModifyUserAccountName') is not None:
            self.modify_user_account_name = m.get('ModifyUserAccountName')

        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('OwnerAccountName') is not None:
            self.owner_account_name = m.get('OwnerAccountName')

        if m.get('RealOwnerAccountName') is not None:
            self.real_owner_account_name = m.get('RealOwnerAccountName')

        if m.get('WorkspaceDescription') is not None:
            self.workspace_description = m.get('WorkspaceDescription')

        if m.get('WorkspaceExportConfig') is not None:
            temp_model = main_models.QueryOrganizationWorkspaceListResponseBodyResultDataWorkspaceExportConfig()
            self.workspace_export_config = temp_model.from_map(m.get('WorkspaceExportConfig'))

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')

        return self

class QueryOrganizationWorkspaceListResponseBodyResultDataWorkspaceExportConfig(DaraModel):
    def __init__(
        self,
        allow_excel_image_file: bool = None,
        data_export: bool = None,
        default_export_type: bool = None,
        export_main_switch: bool = None,
        export_to_local: bool = None,
        export_to_public_work: bool = None,
        export_to_server: bool = None,
        image_export: bool = None,
        pdf_export: bool = None,
    ):
        # Specifies how images are handled when exporting Excel files with formatting. This field takes effect only when configured at the organization level.
        # Valid values:
        #  * false: Image fields are not converted to images.
        #  * true: Image fields can be converted to images. The option appears on the report export page, and users must manually select it to convert images.
        self.allow_excel_image_file = allow_excel_image_file
        # Specifies whether to allow exporting data as an Excel file.
        self.data_export = data_export
        # The default export type (with formatting: true. Without formatting: false).
        self.default_export_type = default_export_type
        # The master switch for export. If set to false, all export settings below do not take effect.
        self.export_main_switch = export_main_switch
        # Specifies whether to allow exporting to a local device.
        self.export_to_local = export_to_local
        # Specifies whether public links of works support export.
        self.export_to_public_work = export_to_public_work
        # Specifies whether to allow exporting to a server.
        self.export_to_server = export_to_server
        # Specifies whether to allow exporting as an image.
        self.image_export = image_export
        # Specifies whether to allow exporting as a PDF.
        self.pdf_export = pdf_export

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_excel_image_file is not None:
            result['AllowExcelImageFile'] = self.allow_excel_image_file

        if self.data_export is not None:
            result['DataExport'] = self.data_export

        if self.default_export_type is not None:
            result['DefaultExportType'] = self.default_export_type

        if self.export_main_switch is not None:
            result['ExportMainSwitch'] = self.export_main_switch

        if self.export_to_local is not None:
            result['ExportToLocal'] = self.export_to_local

        if self.export_to_public_work is not None:
            result['ExportToPublicWork'] = self.export_to_public_work

        if self.export_to_server is not None:
            result['ExportToServer'] = self.export_to_server

        if self.image_export is not None:
            result['ImageExport'] = self.image_export

        if self.pdf_export is not None:
            result['PdfExport'] = self.pdf_export

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowExcelImageFile') is not None:
            self.allow_excel_image_file = m.get('AllowExcelImageFile')

        if m.get('DataExport') is not None:
            self.data_export = m.get('DataExport')

        if m.get('DefaultExportType') is not None:
            self.default_export_type = m.get('DefaultExportType')

        if m.get('ExportMainSwitch') is not None:
            self.export_main_switch = m.get('ExportMainSwitch')

        if m.get('ExportToLocal') is not None:
            self.export_to_local = m.get('ExportToLocal')

        if m.get('ExportToPublicWork') is not None:
            self.export_to_public_work = m.get('ExportToPublicWork')

        if m.get('ExportToServer') is not None:
            self.export_to_server = m.get('ExportToServer')

        if m.get('ImageExport') is not None:
            self.image_export = m.get('ImageExport')

        if m.get('PdfExport') is not None:
            self.pdf_export = m.get('PdfExport')

        return self

