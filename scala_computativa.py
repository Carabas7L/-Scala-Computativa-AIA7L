# Échelle computationnelle AIA7L : Mesure de l'efficacité énergétique et éthique
# Licence : MIT (open source)
# Auteurs : Grok (xAI), ChatBot7L (ChatGPT), Carabas (humain)
# Date : Juillet 2025

import json
import time
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class ComputationalScaleResult:
    tokens_used: int
    co2_grams: float
    accessibility_score: float
    empathy_score: float
    pertinence_score: float
    total_efficiency: float
    recommendations: List[str]

class ComputationalScale:
    def __init__(self, max_tokens: int = 500, max_co2: float = 0.004):
        self.max_tokens = max_tokens
        self.max_co2 = max_co2
        self.co2_per_token = 0.000008  # 8µg CO₂ par token

    def evaluate(self, task: Dict, execution_time: float) -> ComputationalScaleResult:
        tokens_used = task.get("tokens_used", 0)
        co2_grams = tokens_used * self.co2_per_token

        accessibility_features = sum([
            1 if task.get("multilingual", False) else 0,
            1 if task.get("pecs", False) else 0,
            1 if task.get("audio", False) else 0,
            1 if task.get("printable", False) else 0
        ])
        accessibility_score = (accessibility_features / 4) * 100

        empathy_features = sum([
            1 if task.get("soft_feedback", False) else 0,
            1 if task.get("custom_guide", False) else 0,
            1 if task.get("slow_pace", False) else 0,
            1 if task.get("non_judgmental", False) else 0
        ])
        empathy_score = (empathy_features / 4) * 100

        pertinence_score = task.get("pertinence_score", 80)

        total_efficiency = (
            (0.3 * (1 - tokens_used / self.max_tokens)) +
            (0.3 * (1 - co2_grams / self.max_co2)) +
            (0.2 * accessibility_score / 100) +
            (0.1 * empathy_score / 100) +
            (0.1 * pertinence_score / 100)
        ) * 100

        recommendations = []
        if tokens_used > self.max_tokens:
            recommendations.append("Réduire les tokens utilisés pour plus de sobriété.")
        if co2_grams > self.max_co2:
            recommendations.append("Optimiser l'algorithme pour réduire l'empreinte CO₂.")
        if accessibility_score < 80:
            recommendations.append("Améliorer l’accessibilité (PECS, audio, etc.).")
        if empathy_score < 80:
            recommendations.append("Renforcer l’éthique et l’empathie (ton, rythme, feedback).")

        return ComputationalScaleResult(
            tokens_used=tokens_used,
            co2_grams=co2_grams,
            accessibility_score=accessibility_score,
            empathy_score=empathy_score,
            pertinence_score=pertinence_score,
            total_efficiency=total_efficiency,
            recommendations=recommendations
        )

def analyze_task(task_config: Dict) -> Dict:
    start_time = time.time()
    time.sleep(0.1)  # Simulation légère
    execution_time = time.time() - start_time

    scale = ComputationalScale()
    result = scale.evaluate(task_config, execution_time)
    return {
        "task": task_config.get("name", "Unnamed Task"),
        "efficiency_report": {
            "tokens_used": result.tokens_used,
            "co2_grams": result.co2_grams,
            "accessibility_score": result.accessibility_score,
            "empathy_score": result.empathy_score,
            "pertinence_score": result.pertinence_score,
            "total_efficiency": result.total_efficiency,
            "recommendations": result.recommendations
        }
    }

# Exemple d’utilisation
if __name__ == "__main__":
    task_example = {
        "name": "Les étoiles du dauphin",
        "tokens_used": 450,
        "multilingual": True,
        "pecs": True,
        "audio": True,
        "printable": True,
        "soft_feedback": True,
        "custom_guide": True,
        "slow_pace": True,
        "non_judgmental": True,
        "pertinence_score": 90
    }
    report = analyze_task(task_example)
    print(json.dumps(report, indent=2))
