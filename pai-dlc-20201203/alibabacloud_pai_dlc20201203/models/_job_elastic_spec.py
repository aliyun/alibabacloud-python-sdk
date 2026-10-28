# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class JobElasticSpec(DaraModel):
    def __init__(
        self,
        aimaster_docker_image: str = None,
        aimaster_type: str = None,
        edpmax_parallelism: int = None,
        edpmin_parallelism: int = None,
        elastic_strategy: str = None,
        enable_aimaster: bool = None,
        enable_edp: bool = None,
        enable_elastic_training: bool = None,
        enable_ps_job_elastic_ps: bool = None,
        enable_ps_job_elastic_worker: bool = None,
        enable_ps_resource_estimate: bool = None,
        max_parallelism: int = None,
        min_parallelism: int = None,
        psmax_parallelism: int = None,
        psmin_parallelism: int = None,
    ):
        # The AIMaster Docker image.
        self.aimaster_docker_image = aimaster_docker_image
        # The resource specifications for the AIMaster role.
        self.aimaster_type = aimaster_type
        # The maximum EDP parallelism.
        self.edpmax_parallelism = edpmax_parallelism
        # The minimum EDP parallelism.
        self.edpmin_parallelism = edpmin_parallelism
        # The elastic training strategy.
        self.elastic_strategy = elastic_strategy
        # Specifies whether to enable AIMaster.
        self.enable_aimaster = enable_aimaster
        # Specifies whether to enable EDP.
        self.enable_edp = enable_edp
        # Specifies whether to enable elastic training.
        self.enable_elastic_training = enable_elastic_training
        # Specifies whether to enable the elastic PS feature.
        self.enable_ps_job_elastic_ps = enable_ps_job_elastic_ps
        # Specifies whether to enable elastic workers for PS jobs.
        self.enable_ps_job_elastic_worker = enable_ps_job_elastic_worker
        # Specifies whether to enable PS resource estimation.
        self.enable_ps_resource_estimate = enable_ps_resource_estimate
        # The maximum parallelism.
        self.max_parallelism = max_parallelism
        # The minimum parallelism.
        self.min_parallelism = min_parallelism
        # The maximum PS parallelism.
        self.psmax_parallelism = psmax_parallelism
        # The minimum PS parallelism.
        self.psmin_parallelism = psmin_parallelism

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aimaster_docker_image is not None:
            result['AIMasterDockerImage'] = self.aimaster_docker_image

        if self.aimaster_type is not None:
            result['AIMasterType'] = self.aimaster_type

        if self.edpmax_parallelism is not None:
            result['EDPMaxParallelism'] = self.edpmax_parallelism

        if self.edpmin_parallelism is not None:
            result['EDPMinParallelism'] = self.edpmin_parallelism

        if self.elastic_strategy is not None:
            result['ElasticStrategy'] = self.elastic_strategy

        if self.enable_aimaster is not None:
            result['EnableAIMaster'] = self.enable_aimaster

        if self.enable_edp is not None:
            result['EnableEDP'] = self.enable_edp

        if self.enable_elastic_training is not None:
            result['EnableElasticTraining'] = self.enable_elastic_training

        if self.enable_ps_job_elastic_ps is not None:
            result['EnablePsJobElasticPS'] = self.enable_ps_job_elastic_ps

        if self.enable_ps_job_elastic_worker is not None:
            result['EnablePsJobElasticWorker'] = self.enable_ps_job_elastic_worker

        if self.enable_ps_resource_estimate is not None:
            result['EnablePsResourceEstimate'] = self.enable_ps_resource_estimate

        if self.max_parallelism is not None:
            result['MaxParallelism'] = self.max_parallelism

        if self.min_parallelism is not None:
            result['MinParallelism'] = self.min_parallelism

        if self.psmax_parallelism is not None:
            result['PSMaxParallelism'] = self.psmax_parallelism

        if self.psmin_parallelism is not None:
            result['PSMinParallelism'] = self.psmin_parallelism

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AIMasterDockerImage') is not None:
            self.aimaster_docker_image = m.get('AIMasterDockerImage')

        if m.get('AIMasterType') is not None:
            self.aimaster_type = m.get('AIMasterType')

        if m.get('EDPMaxParallelism') is not None:
            self.edpmax_parallelism = m.get('EDPMaxParallelism')

        if m.get('EDPMinParallelism') is not None:
            self.edpmin_parallelism = m.get('EDPMinParallelism')

        if m.get('ElasticStrategy') is not None:
            self.elastic_strategy = m.get('ElasticStrategy')

        if m.get('EnableAIMaster') is not None:
            self.enable_aimaster = m.get('EnableAIMaster')

        if m.get('EnableEDP') is not None:
            self.enable_edp = m.get('EnableEDP')

        if m.get('EnableElasticTraining') is not None:
            self.enable_elastic_training = m.get('EnableElasticTraining')

        if m.get('EnablePsJobElasticPS') is not None:
            self.enable_ps_job_elastic_ps = m.get('EnablePsJobElasticPS')

        if m.get('EnablePsJobElasticWorker') is not None:
            self.enable_ps_job_elastic_worker = m.get('EnablePsJobElasticWorker')

        if m.get('EnablePsResourceEstimate') is not None:
            self.enable_ps_resource_estimate = m.get('EnablePsResourceEstimate')

        if m.get('MaxParallelism') is not None:
            self.max_parallelism = m.get('MaxParallelism')

        if m.get('MinParallelism') is not None:
            self.min_parallelism = m.get('MinParallelism')

        if m.get('PSMaxParallelism') is not None:
            self.psmax_parallelism = m.get('PSMaxParallelism')

        if m.get('PSMinParallelism') is not None:
            self.psmin_parallelism = m.get('PSMinParallelism')

        return self

