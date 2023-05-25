def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    countador = 0
    for time_entrad, time_saida in permanence_period:
        if not isinstance(time_entrad, int) or not isinstance(time_saida, int):
            return None
        if time_entrad <= target_time <= time_saida:
            countador += 1

    return countador
