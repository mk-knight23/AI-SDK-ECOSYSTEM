<script lang="ts">
  const appName = 'DevSquad';
</script>

<main class="container">
  <h1>Hello World from {appName}</h1>
  <p>Welcome to your SvelteKit application!</p>
  <div class="card">
    <p>Built with SvelteKit + Node.js</p>
  </div>
</main>

<style>
  .container {
    max-width: 800px;
    margin: 0 auto;
    padding: 2rem;
    text-align: center;
    font-family: system-ui, -apple-system, sans-serif;
  }

  h1 {
    color: #ff3e00;
    font-size: 2.5rem;
    margin-bottom: 1rem;
  }

  .card {
    background: #f5f5f5;
    border-radius: 8px;
    padding: 1.5rem;
    margin-top: 2rem;
  }

  .card p {
    color: #666;
    margin: 0;
  }
</style>
