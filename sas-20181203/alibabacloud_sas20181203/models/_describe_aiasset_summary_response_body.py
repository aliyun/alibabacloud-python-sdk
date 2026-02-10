# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeAIAssetSummaryResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeAIAssetSummaryResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeAIAssetSummaryResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAIAssetSummaryResponseBodyData(DaraModel):
    def __init__(
        self,
        aispm_risk_asset_cnt: int = None,
        ecs_asset_cnt: int = None,
        exposed_risk_asset_cnt: int = None,
        image_asset_cnt: int = None,
        lingjun_asset_cnt: int = None,
        pai_container_cnt: int = None,
        pai_instance_cnt: int = None,
        pai_serverless_asset_cnt: int = None,
        sensitive_summary: main_models.DescribeAIAssetSummaryResponseBodyDataSensitiveSummary = None,
        snapshot_asset_cnt: int = None,
        total_asset_cnt: int = None,
        total_risk_cnt: int = None,
        vul_risk_asset_cnt: int = None,
    ):
        # The number of cloud assets with AI security posture management risks.
        self.aispm_risk_asset_cnt = aispm_risk_asset_cnt
        # The number of servers on which AI components are installed.
        self.ecs_asset_cnt = ecs_asset_cnt
        # The number of servers that have exposed AI components.
        self.exposed_risk_asset_cnt = exposed_risk_asset_cnt
        # The number of AI images.
        self.image_asset_cnt = image_asset_cnt
        # The number of LINGJUN assets.
        self.lingjun_asset_cnt = lingjun_asset_cnt
        # The number of container image assets in PAI.
        self.pai_container_cnt = pai_container_cnt
        # The total number of cloud asset instances in Platform for AI (PAI).
        self.pai_instance_cnt = pai_instance_cnt
        # The number of serverless assets in PAI.
        self.pai_serverless_asset_cnt = pai_serverless_asset_cnt
        # The statistics on assets that have AI-related keys are stored in plaintext.
        self.sensitive_summary = sensitive_summary
        # The number of AI snapshots.
        self.snapshot_asset_cnt = snapshot_asset_cnt
        # The total number of AI assets.
        self.total_asset_cnt = total_asset_cnt
        # The total number of assets with AI risks.
        self.total_risk_cnt = total_risk_cnt
        # The number of servers with AI application vulnerabilities.
        self.vul_risk_asset_cnt = vul_risk_asset_cnt

    def validate(self):
        if self.sensitive_summary:
            self.sensitive_summary.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aispm_risk_asset_cnt is not None:
            result['AispmRiskAssetCnt'] = self.aispm_risk_asset_cnt

        if self.ecs_asset_cnt is not None:
            result['EcsAssetCnt'] = self.ecs_asset_cnt

        if self.exposed_risk_asset_cnt is not None:
            result['ExposedRiskAssetCnt'] = self.exposed_risk_asset_cnt

        if self.image_asset_cnt is not None:
            result['ImageAssetCnt'] = self.image_asset_cnt

        if self.lingjun_asset_cnt is not None:
            result['LingjunAssetCnt'] = self.lingjun_asset_cnt

        if self.pai_container_cnt is not None:
            result['PaiContainerCnt'] = self.pai_container_cnt

        if self.pai_instance_cnt is not None:
            result['PaiInstanceCnt'] = self.pai_instance_cnt

        if self.pai_serverless_asset_cnt is not None:
            result['PaiServerlessAssetCnt'] = self.pai_serverless_asset_cnt

        if self.sensitive_summary is not None:
            result['SensitiveSummary'] = self.sensitive_summary.to_map()

        if self.snapshot_asset_cnt is not None:
            result['SnapshotAssetCnt'] = self.snapshot_asset_cnt

        if self.total_asset_cnt is not None:
            result['TotalAssetCnt'] = self.total_asset_cnt

        if self.total_risk_cnt is not None:
            result['TotalRiskCnt'] = self.total_risk_cnt

        if self.vul_risk_asset_cnt is not None:
            result['VulRiskAssetCnt'] = self.vul_risk_asset_cnt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AispmRiskAssetCnt') is not None:
            self.aispm_risk_asset_cnt = m.get('AispmRiskAssetCnt')

        if m.get('EcsAssetCnt') is not None:
            self.ecs_asset_cnt = m.get('EcsAssetCnt')

        if m.get('ExposedRiskAssetCnt') is not None:
            self.exposed_risk_asset_cnt = m.get('ExposedRiskAssetCnt')

        if m.get('ImageAssetCnt') is not None:
            self.image_asset_cnt = m.get('ImageAssetCnt')

        if m.get('LingjunAssetCnt') is not None:
            self.lingjun_asset_cnt = m.get('LingjunAssetCnt')

        if m.get('PaiContainerCnt') is not None:
            self.pai_container_cnt = m.get('PaiContainerCnt')

        if m.get('PaiInstanceCnt') is not None:
            self.pai_instance_cnt = m.get('PaiInstanceCnt')

        if m.get('PaiServerlessAssetCnt') is not None:
            self.pai_serverless_asset_cnt = m.get('PaiServerlessAssetCnt')

        if m.get('SensitiveSummary') is not None:
            temp_model = main_models.DescribeAIAssetSummaryResponseBodyDataSensitiveSummary()
            self.sensitive_summary = temp_model.from_map(m.get('SensitiveSummary'))

        if m.get('SnapshotAssetCnt') is not None:
            self.snapshot_asset_cnt = m.get('SnapshotAssetCnt')

        if m.get('TotalAssetCnt') is not None:
            self.total_asset_cnt = m.get('TotalAssetCnt')

        if m.get('TotalRiskCnt') is not None:
            self.total_risk_cnt = m.get('TotalRiskCnt')

        if m.get('VulRiskAssetCnt') is not None:
            self.vul_risk_asset_cnt = m.get('VulRiskAssetCnt')

        return self

class DescribeAIAssetSummaryResponseBodyDataSensitiveSummary(DaraModel):
    def __init__(
        self,
        container_image_cnt: int = None,
        ecs_cnt: int = None,
        image_cnt: int = None,
        snapshot_cnt: int = None,
        total_cnt: int = None,
    ):
        # The number of images that have AI-related keys are stored in plaintext detected by image scan.
        self.container_image_cnt = container_image_cnt
        # The number of servers that have AI-related keys are stored in plaintext detected by agentless scan.
        self.ecs_cnt = ecs_cnt
        # The number of images that have AI-related keys are stored in plaintext detected by agentless scan.
        self.image_cnt = image_cnt
        # The number of snapshots that have AI-related keys are stored in plaintext detected by agentless scan.
        self.snapshot_cnt = snapshot_cnt
        # The total number of assets that have AI-related keys are stored in plaintext.
        self.total_cnt = total_cnt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.container_image_cnt is not None:
            result['ContainerImageCnt'] = self.container_image_cnt

        if self.ecs_cnt is not None:
            result['EcsCnt'] = self.ecs_cnt

        if self.image_cnt is not None:
            result['ImageCnt'] = self.image_cnt

        if self.snapshot_cnt is not None:
            result['SnapshotCnt'] = self.snapshot_cnt

        if self.total_cnt is not None:
            result['TotalCnt'] = self.total_cnt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerImageCnt') is not None:
            self.container_image_cnt = m.get('ContainerImageCnt')

        if m.get('EcsCnt') is not None:
            self.ecs_cnt = m.get('EcsCnt')

        if m.get('ImageCnt') is not None:
            self.image_cnt = m.get('ImageCnt')

        if m.get('SnapshotCnt') is not None:
            self.snapshot_cnt = m.get('SnapshotCnt')

        if m.get('TotalCnt') is not None:
            self.total_cnt = m.get('TotalCnt')

        return self

