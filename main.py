import subprocess
import time
import resource
import os

def benchmark(iterations):
  times = []
  memory_usage = []

  try:
    absolute_dir = os.path.abspath('./planner-for-relevant-policies/src/prp')
    execute_dir = [absolute_dir, 'domain.pddl', 'p01.pddl']
    
    if not os.path.exists(execute_dir):
      print(f"Erro: O executável não foi encontrado em {execute_dir}")

    if not os.access(execute_dir, os.X_OK):
      print(f"Erro: Permissão de execução negada para {execute_dir}")

  except FileNotFoundError:
    print("Error")

  for i in range(iterations):
    start_memory = resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
    start_time = time.time()

    try:
      result = subprocess.run(execute_dir, check=True, capture_output=True)
      output_stdout = result.stdout.decode('utf-8')
      output_stderr = result.stderr.decode('utf-8')

      print(output_stdout)
      print(output_stderr)
    except subprocess.CalledProcessError as e:
      print(f"Erro durante a execução: {e}")

    end_time = time.time()
    end_memory = resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss

    elapsed_time = end_time - start_time
    memory_used = end_memory - start_memory
    
    times.append(elapsed_time)
    memory_usage.append(memory_used)

    print(f"Iteração {i + 1}: {elapsed_time} segundos, Uso de Memória: {memory_used} KB")


  avg_time = sum(times) / iterations
  avg_memory = sum(memory_usage) / iterations
  print(f"Tempo médio de execução para {iterations} iterações: {avg_time} segundos")
  print(f"Uso médio de memória para {iterations} iterações: {avg_memory} KB")

iterations_number = 1

benchmark(iterations_number)